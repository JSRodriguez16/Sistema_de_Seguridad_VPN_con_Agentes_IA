Received15September2025;revised10October2025;accepted18October2025.Dateofpublication24October2025;dateofcurrentversion3November2025.
DigitalObjectIdentifier10.1109/OJCOMS.2025.3625534
Network Traffic Classification Using Self-Supervised
Learning and Confident Learning
EHSANESLAMI (StudentMember,IEEE),ANDWALAAHAMOUDA (Senior Member,IEEE)
DepartmentofElectricalandComputerEngineering,ConcordiaUniversity,Montreal,QCH3G1M8,Canada
CORRESPONDINGAUTHOR:W.HAMOUDA(e-mail:walaa.hamouda@concordia.ca)
ABSTRACT Network traffic classification (NTC) is vital for efficient network management, security,
and performance optimization, particularly with 5G/6G technologies. Traditional methods, such as deep
packet inspection (DPI) and port-based identification, struggle with the rise of encrypted traffic and
dynamicportallocations.Supervisedlearningmethodsprovideviablealternativesbutrelyonlargelabeled
datasets, which are difficult to acquire given the diversity and volume of network traffic. Meanwhile,
unsupervisedlearningmethods,whilelessreliantonlabeleddata,oftenexhibitloweraccuracy.Toaddress
these limitations, we propose a novel framework that first leverages Self-Supervised Learning (SSL)
with techniques such as autoencoders (AE) or Tabular Contrastive Learning (TabCL) to generate pseudo-
labels from extensive unlabeled datasets, addressing the challenge of limited labeled data. We then apply
traffic-adapted Confident Learning (CL) to refine these pseudo-labels, enhancing classification precision
by mitigating the impact of noise. Our proposed framework offers a generalizable solution that minimizes
the need for extensive labeled data while delivering high accuracy. Extensive simulations and evaluations
using three datasets (ISCX VPN-nonVPN, self-generated dataset, and UCDavis–QUIC) demonstrate that
our method achieves superior accuracy compared to state-of-the-art techniques in classifying network
traffic.
INDEX TERMS Network traffic classification, Internet traffic classification, self-supervised learning,
contrastive learning, application identification.
I. INTRODUCTION management,predictivemaintenance,andreal-timeanomaly
NETWORK traffic classification (NTC) is a cornerstone detection [7], [8].
ofmodernnetworkmanagementandsecurity,enabling For NTC, traditional approaches such as port-based
theidentificationofapplicationsandservices,suchasvideo- identificationandDeepPacketInspection(DPI)havebecome
streaming or data traffic applications, based on their traffic inadequate. Port-based methods fail due to dynamic port
patterns [1]. This capability supports essential functions usage, while DPI struggles with the prevalence of encrypted
like Quality of Service (QoS) provisioning [2], anomaly traffic [9], [10]. As a result, modern supervised and
detection, and traffic engineering. The exponential growth representation-learning approaches now dominate. Machine
of Internet traffic [3], driven by the increasing number Learning (ML) and Deep Learning (DL) methods can
of connected devices, the expansion of cloud computing, classify traffic using statistical features [11] and time-series
and the rise of Artificial Intelligence (AI)–driven services, features [12]. Supervised learning trains models on labeled
highlights the need for effective NTC methods [4]. The datasetsandcanachievestate-of-the-art(SOTA)performance
deployment of 5G and upcoming 6G networks has fur- when sufficient labels are available. For instance, Support
ther complicated network traffic [5], introducing diverse Vector Machines (SVM) and logistic regression remain
requirementsfornetworkslicing,edgecomputing,andUltra- competitive in Software-Defined Networking (SDN); neural
Reliable Low-Latency Communications (URLLC), making networks report strong accuracy and robustness on common
robust classification increasingly essential [6]. AI plays a benchmarks; supervisedcontrastive methods achieve leading
vitalroleinmodernnetworking,facilitatingintelligenttraffic results under label imbalance; and adversarially trained
(cid:2)c 2025TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution4.0License.
Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/
9100 VOLUME6,2025

models sustain accuracy under perturbations [13], [14], designs ensure that AE focuses on fidelity in reconstruction,
[15], [16]. Unsupervised learning, in contrast, does not while TabCL emphasizes similarity between related views.
require labels and can discover patterns independently [4]. We then fuse the SSL predictions via a confidence/margin
More recently, Self-Supervised Learning (SSL) has shown voting rule so that the more decisive branch prevails when
promise by leveraging abundant unlabeled traffic to learn thetwodisagree.Second,inspiredbyCL,wedecouplenoise
representations and produce pseudo-labels with a small estimationfromthefinalclassifierandtreattheSSLpseudo-
labeled set, reducing reliance on extensive labeled datasets labels as inputs to a CL module. Using k-fold out-of-sample
and improving coverage [17]. For example, contrastive prediction probabilities, we estimate the confident joint and
pretraining on flow images achieves strong few-shot and introduce adaptations tailored to network traffic flows: per-
transfer performance; transformer pretraining that tokenizes class, quantile thresholds (rather than means thresholds) for
packet/flow bytes and transfers to downstream NTC tasks; robustness under skew; a logistic weighting that smoothly
and masked flow-image autoencoding advances SOTA SSL down-weights uncertain pseudo-labels instead of discarding
representations [18], [19], [20]. SSL tailored to encrypted data; and a balanced retention constraint that aligns each
protocols likewise reports high accuracy with only a small class’s retained training mass with its CL-estimated clean
labeled seed [21]. fraction[26].Third,wetrainthedownstreamclassifieronthe
Despite this progress, important challenges remain. For full pseudo-labeled pool using a weighted symmetric cross-
supervised learning, labeling network traffic is resource- entropy objective, where per-sample weights, derived from
intensive and costly, and labeled datasets often fail to reflect theCLmoduleviaout-of-sampleprobabilities,down-weight
the full diversity of real-world traffic, which reduces model uncertain pseudo-labels while retaining all data.
generalizability [22], [23], [24]. Recent analyses show that Although recent SOTA methods attain high accuracy,
capture-specific fields (e.g., timestamps/MAC/IP/ports) in important gaps persist—namely, reliance on scarce labels
common NTC benchmarks raise supervised accuracy; once in supervised learning, limited precision in unsupervised
properly anonymized, accuracy drops sharply, indicating methods, noise in SSL pseudo-labels, and per-class cal-
weak generalization [25]. Unsupervised methods, while ibration/imbalance issues. Our framework addresses these
label-free, often struggle to capture the complex pat- gaps by pairing NTC-specific SSL (constraint-aware views,
terns needed for precise traffic classification and typically dual-head temperatures, SSL fusion) with NTC-adapted CL
underperform supervised methods [4]. While SSL offers (quantile thresholds, logistic weighting, balanced retention)
significant benefits by leveraging unlabeled data, SSL- before final training. The contributions of this paper are as
| derived     | pseudo-labels | can     | contain  | noise        | due   | to             | imperfect  | follows:      |     |           |            |          |               |             |     |
| ----------- | ------------- | ------- | -------- | ------------ | ----- | -------------- | ---------- | ------------- | --- | --------- | ---------- | -------- | ------------- | ----------- | --- |
| pretext     | accuracy;     | if used | directly | to           | train | the downstream |            |               |     |           |            |          |               |             |     |
|             |               |         |          |              |       |                |            | 1) We propose |     | the first | end-to-end |          | framework     | integrating |     |
| classifier, | these         | errors  | degrade  | performance. |       | A              | principled |               |     |           |            |          |               |             |     |
|             |               |         |          |              |       |                |            | SSL and       | CL  | for NTC   | that       | produces | pseudo-labels |             | via |
waytocopewithnoisylabelsisconfidentlearning(CL)[26],
|                 |           |                   |      |               |        |          |          | AE and            | TabCL,                | then | denoises      |              | them with      | CL         | before   |
| --------------- | --------- | ----------------- | ---- | ------------- | ------ | -------- | -------- | ----------------- | --------------------- | ---- | ------------- | ------------ | -------------- | ---------- | -------- |
| which estimates |           | class-conditional |      | label         | errors | from     | out-of-  |                   |                       |      |               |              |                |            |          |
|                 |           |                   |      |               |        |          |          | final training.   |                       | Our  | framework     | incorporates |                | innovative |          |
| sample          | predicted | probabilities     |      | together      | with   | the      | observed |                   |                       |      |               |              |                |            |          |
|                 |           |                   |      |               |        |          |          | extensions        | to                    | both | components    |              | that enhance   |            | accuracy |
| (pseudo)        | labels    | and constructs    |      | the confident |        | joint—a  | matrix   |                   |                       |      |               |              |                |            |          |
|                 |           |                   |      |               |        |          |          | and label         | efficiency            |      | beyond        | standard     | approaches.    |            |          |
| summarizing     |           | how often         | each | observed      | class  | appears  |          | to                |                       |      |               |              |                |            |          |
|                 |           |                   |      |               |        |          |          | 2) We demonstrate |                       | the  | effectiveness |              | of             | our        | enhanced |
| belong          | to each   | (latent)          | true | class—thus    |        | enabling | noise-   |                   |                       |      |               |              |                |            |          |
|                 |           |                   |      |               |        |          |          | AE with           | constraint-consistent |      |               |              | reconstruction |            | and      |
awarefilteringorreweightingofpseudo-labels.BringingCL
|            |              |           |              |                |       |          |     | NTC-tailored          |     | TabCL          |       | with | class-conditioned, |             |      |
| ---------- | ------------ | --------- | ------------ | -------------- | ----- | -------- | --- | --------------------- | --- | -------------- | ----- | ---- | ------------------ | ----------- | ---- |
| principles | to NTC       | addresses | pseudo-label |                | noise | directly | and |                       |     |                |       |      |                    |             |      |
|            |              |           |              |                |       |          |     | constraint-preserving |     |                | views | and  | dual-head          | projections |      |
| provides   | a principled | bridge    | from         | representation |       | learning |     | to                    |     |                |       |      |                    |             |      |
|            |              |           |              |                |       |          |     | for generating        |     | higher-quality |       |      | pseudo-labels      |             | from |
reliable training.
unlabeleddatathansimpleAEsortheoriginalTabCL.
| To address           |           | the aforementioned |               | challenges,   |               | this         | paper     |               |             |            |                 |            |             |               |            |
| -------------------- | --------- | ------------------ | ------------- | ------------- | ------------- | ------------ | --------- | ------------- | ----------- | ---------- | --------------- | ---------- | ----------- | ------------- | ---------- |
|                      |           |                    |               |               |               |              |           | 3) We show    | that        | our        | traffic-adapted |            | CL          | improves      | clas-      |
| proposes             | a novel   | framework          |               | that combines |               | SSL          | and CL    |               |             |            |                 |            |             |               |            |
|                      |           |                    |               |               |               |              |           | sification    | accuracy    |            | over the        | original   | CL          | by            | replacing  |
| for NTC.             | First,    | our approach       |               | uses SSL      | to generate   |              | pseudo-   |               |             |            |                 |            |             |               |            |
|                      |           |                    |               |               |               |              |           | mean          | thresholds  | with       | per-class       |            | quantile    | thresholds    | for        |
| labels for           | unlabeled | traffic            | flows         | by            | pretraining   |              | with an   |               |             |            |                 |            |             |               |            |
|                      |           |                    |               |               |               |              |           | greater       | robustness  |            | to imbalance    |            | and         | skew,         | incorpo-   |
| unlabeled            | dataset   | and                | fine-tuning   | with          | a             | small        | labeled   |               |             |            |                 |            |             |               |            |
|                      |           |                    |               |               |               |              |           | rating        | logistic    | weights    | for             | smoother   |             | attenuation   | of         |
| dataset.             | We        | develop two        | complementary |               |               | SSL          | branches: |               |             |            |                 |            |             |               |            |
|                      |           |                    |               |               |               |              |           | uncertain     | labels,     | and        | balanced        | retention  |             | guided        | by the     |
| (i) an autoencoder   |           | (AE)               | reconstructs  |               | heterogeneous |              | (con-     |               |             |            |                 |            |             |               |            |
|                      |           |                    |               |               |               |              |           | confident     | joint       | to improve |                 | noise      | robustness. |               |            |
| tinuous/categorical) |           | flow               | features      | while         | softly        |              | enforcing |               |             |            |                 |            |             |               |            |
|                      |           |                    |               |               |               |              |           | 4) We conduct |             | a thorough |                 | evaluation |             | and           | ablations, |
| algebraic            | relations | among              | them          | for more      | plausible     |              | outputs,  |               |             |            |                 |            |             |               |            |
|                      |           |                    |               |               |               |              |           | including     | simulations |            | to              | create     | a realistic |               | network    |
| and (ii)             | Tabular   | Contrastive        |               | Learning      | (TabCL)       |              | [27] with |               |             |            |                 |            |             |               |            |
|                      |           |                    |               |               |               |              |           | traffic       | dataset,    | and        | assess          | our        | model’s     | performance   |            |
| class-conditioned    |           | replacement        |               | and dual-head |               | projections. |           |               |             |            |                 |            |             |               |            |
|                      |           |                    |               |               |               |              |           | by comparing  |             | it to      | existing        | methods,   |             | demonstrating |            |
| This enhanced        |           | TabCL              | method        | creates       | augmented     |              | views     |               |             |            |                 |            |             |               |            |
|                      |           |                    |               |               |               |              |           | superior      | accuracy    | and        | macro-F1        |            | under       | limited       | labels.    |
| by replacing         | features  | from               | the           | same          | class         | distribution | and       |               |             |            |                 |            |             |               |            |
projects them through separate heads for continuous and The rest of this paper is organized as follows: Section II
categorical slices to handle feature heterogeneity. These reviewsrelatedworkinNTCandSSL.SectionIIIformalizes
| VOLUME6,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 9101 |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |

ESLAMIANDHAMOUDA:NTCUSINGSSLANDCL
the problem, assumptions, and notation. Section IV details boost label efficiency, reaching 94.00% class accuracy on
the proposed framework. Section V presents the simulation QUIC with 150 labels. Despite their success, these super-
andexperimentalresults,andSectionVIconcludesthepaper. vised DL methods rely heavily on large labeled datasets,
|                 |     |     |     |     | which are             | costly | and may | not generalize |     | across diverse |
| --------------- | --- | --- | --- | --- | --------------------- | ------ | ------- | -------------- | --- | -------------- |
| II. RELATEDWORK |     |     |     |     | network environments. |        |         |                |     |                |
ThissectionprovidesadetailedreviewoftheSOTAresearch, On the other hand, unsupervised learning methods have
focusing on ML, supervised and unsupervised DL, and SSL been explored for NTC to circumvent the need for
methods.
|     |     |     |     |     | labeled datasets | [36],    | [37].    | Zhang      | et al. | [36] proposed |
| --- | --- | --- | --- | --- | ---------------- | -------- | -------- | ---------- | ------ | ------------- |
|     |     |     |     |     | an adversarial   | training | and deep | clustering |        | method. Their |
A. TRADITIONALANDMACHINELEARNINGFORNTC approach achieved a multi-classification accuracy of 92.2%.
Early NTC relied on port-based methods and DPI. Reference [37] propose an unsupervised deep multi-source
Reference[28]proposesBitProb,whichencodesflowsasbit domain-adaptation NTC model (multi-scale features and
signatures and uses a probabilistic automaton for protocol alignment) that achieves 89% accuracy. These methods
assignment.Thesetraditionalmethodsstrugglewithdynamic cluster flows by similarity without labels; despite this
ports and encrypted traffic. ML is one of the promising advantage, they generally lag behind supervised learning
solutions for NTC [13], [29]. For example, [29] utilized in accuracy, particularly in complex and diverse traffic
| supervised | ML models such | as Decision | Tree  | and Random  | scenarios. |     |     |     |     |     |
| ---------- | -------------- | ----------- | ----- | ----------- | ---------- | --- | --- | --- | --- | --- |
| Forest in  | an SDN context | for NTC.    | Serag | et al. [13] |            |     |     |     |     |     |
demonstratedclassicalMLalgorithmslikeSVMandLogistic C. SELF-SUPERVISEDLEARNINGFORNTC
Regression for SDN traffic classification. These approaches By learning directly from unlabeled data, SSL methods
handle encrypted and dynamic traffic well using statistical reduce reliance on large labeled datasets [18], [19], [20],
and flow features, but remain constrained by the high [21], [38], [39]. Towhid and Shahriar [21] applied SSL
labeling demand of supervised learning. techniques to encrypted NTC, achieving high accuracy with
|     |     |     |     |     | minimal labeled | data     | across     | multiple | public | datasets such |
| --- | --- | --- | --- | --- | --------------- | -------- | ---------- | -------- | ------ | ------------- |
|     |     |     |     |     | as Quick UDP    | Internet | Connection | (QUIC)   | [40]   | and ISCX      |
B. SUPERVISEDANDUNSUPERVISEDDEEPLEARNING
| FORNTC |     |     |     |     | VPN-nonVPN | datasets. | Reference | [18] | proposes | an SSL |
| ------ | --- | --- | --- | --- | ---------- | --------- | --------- | ---- | -------- | ------ |
DL has shown promise in NTC due to its ability to learn framework for traffic classification that utilizes the FlowPic
complex patterns from raw data [14], [15], [16], [30], method.Thisapproachtransformsnetworkflowdatainto2D
[31], [32], [33], [34]. For instance, Lotfollahi et al. [30] histogram images, which are then processed by contrastive
proposed “Deep Packet,” using Stacked Autoencoders representation learning and CNNs. ET-BERT [19] is a
(SAEs) and Convolutional Neural Networks (CNNs) to Transformer-based framework for NTC that learns contextu-
classify encrypted traffic on the ISCX VPN-nonVPN alized datagram representations from large unlabeled traffic
dataset [12], while reducing manual feature engineering via andthenfine-tuneswithfewlabels.ItusesDatagram2Token
+
learned representations. Reference [31] introduced a DL (BURST extraction byte-bigram tokenization) and two
approach combining CNN and Recurrent Neural Networks traffic-tailored pretext tasks—Masked BURST Modeling
(RNNs), achieving SOTA performance on the CIC-IOT (MBM) and Same-origin BURST Prediction (SBP)—with a
dataset [35]. In [14], IBNN adds an information-bottleneck 12-layer bidirectional Transformer, supporting packet- and
layer to a CNN plus a fully connected classifier to retain flow-level fine-tuning. ET-BERT delivers strong macro-F1
(> 96%)
task-relevant features while discarding noise, achieving and accuracy on different datasets. YaTC [20]
97.6% and 98.2% on ISCX datasets, indicating stronger couplesamasked-autoencoder(MAE)pluspacket/flow-level
generalization and robustness. Ma et al. [15] introduce Transformer attention over a multi-level flow representation
BalancedSupervisedContrastiveLearning(BSCL),mapping (MFR) byte layout. Pretrained on large unlabeled traffic and
packetstoimagesforResNet-50trainingwithcontrastiveand fine-tunedwithfewlabels,YaTCachievesSOTAonmultiple
imbalance-aware losses; on the ISCX2016, it achieves high NTCdatasets.TheseadvancementshighlightSSL’spotential
traffic-typeaccuracy.Reference[32]proposesaCNN–Long- toreducedependency onlabeleddata,makingitakeyfocus
| Short-Term    | Memory (LSTM)   | AE that  | learns spatiotemporal |           | of our work. |     |     |     |     |     |
| ------------- | --------------- | -------- | --------------------- | --------- | ------------ | --- | --- | --- | --- | --- |
| flow features | from statistics | and then | classifies            | in latent |              |     |     |     |     |     |
space, reaching near-perfect accuracy on 1.42M flows (4 D. COMPARISONWITHEXISTINGMETHODS
classes) while remaining robust to imbalance. Xiao et al.’s We integrate constraint-aware SSL methods for pseudo-
RBLJAN [16] is a supervised DL model that processes labeling, a traffic-adapted CL module to denoise them, and
headers/payloads with joint attention and adversarial train- a weighted Multilayer Perceptron (MLP) for final training.
ing for packet-to-flow classification. On various datasets, This differs from supervised NTC methods [13], [14], [15],
RBLJAN reports 98% average F1 and about 97% accuracy. [16],[29],[30],[31],[32],[33],[34],whichrequireextensive
MTEFU[34]usesmulti-tasksupervision(class+bandwidth
|     |     |     |     |     | labels, by | leveraging | unlabeled | traffic | while | controlling |
| --- | --- | --- | --- | --- | ---------- | ---------- | --------- | ------- | ----- | ----------- |
+ duration) with shared CNN, SAE, Gated Recurrent Unit label noise. Our constraint-consistent reconstruction AE
(GRU), and LSTM backbones with early-packet inputs to and constraint-aware TabCL with dual-head projections,
| 9102 |     |     |     |     |     |     |     |     |     | VOLUME6,2025 |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ |

TABLE1. Listofnotations.
| combined    | with traffic-adapted |      | CL extensions, |           | yield better |     |     |     |     |
| ----------- | -------------------- | ---- | -------------- | --------- | ------------ | --- | --- | --- | --- |
| scalability | and accuracy         | than | prior SSL      | baselines | [18], [19],  |     |     |     |     |
| [20], [21], | [38], [39].          |      |                |           |              |     |     |     |     |
III. PROBLEMDEFINITIONANDFORMULATION
| We consider     | NTC            | over K application |             | classes from | hetero-    |     |     |     |     |
| --------------- | -------------- | ------------------ | ----------- | ------------ | ---------- | --- | --- | --- | --- |
|                 |                |                    | ={(x,y)}|Ds | |            |            |     |     |     |     |
| geneous         | flow features. | Let D              |             | denote       | a small    |     |     |     |     |
|                 |                |                    | s i         | i i=1        |            |     |     |     |     |
|                 |                | ∈ {1,...,K}        |             | =            | {x}|Dl |   |     |     |     |     |
| labeled         | dataset with   | y i                |             | and D l      | j j=1      | a   |     |     |     |
| large unlabeled | dataset        | drawn              | from        | the same     | deployment |     |     |     |     |
∈ Rd
| domain.  | Each flow | x                 | comprises | continuous | attributes  |     |     |     |     |
| -------- | --------- | ----------------- | --------- | ---------- | ----------- | --- | --- | --- | --- |
| x (e.g., | counts,   | bytes, durations, | rates)    | and        | categorical |     |     |     |     |
cont
| attributesx | (e.g.,protocol,direction),encodednumerically. |     |     |     |     |     |     |     |     |
| ----------- | --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
cat
| Continuous     | attributes         | include              | statistical        | features     | (e.g., total |     |     |     |     |
| -------------- | ------------------ | -------------------- | ------------------ | ------------ | ------------ | --- | --- | --- | --- |
| packets,       | total bytes,       | flow duration,       | average            | packet       | size) and    |     |     |     |     |
| time-series    | features           | (e.g., inter-arrival |                    | times, burst | patterns).   |     |     |     |     |
| These features | are                | essential            | for classification | because      | they         |     |     |     |     |
| capture        | both the aggregate | behavior             | and                | temporal     | dynamics     |     |     |     |     |
of traffic.
| Given | D and | D, our objective | is  | to learn a | multiclass |     |     |     |     |
| ----- | ----- | ---------------- | --- | ---------- | ---------- | --- | --- | --- | --- |
s l
| classifier | C : Rd | →{1,...,K} | that | attains high | accuracy |     |     |     |     |
| ---------- | ------ | ---------- | ---- | ------------ | -------- | --- | --- | --- | --- |
final
| and macro-F1     | under             | scarce   | labels by      | leveraging    | D l via |     |     |     |     |
| ---------------- | ----------------- | -------- | -------------- | ------------- | ------- | --- | --- | --- | --- |
| self-supervision | and               | training | on a           | noise-aware   | pseudo- |     |     |     |     |
| labeled          | pool. Concretely, | we       | first generate | pseudo-labels | for     |     |     |     |     |
| D through        | two complementary |          | SSL            | branches      | adapted | to  |     |     |     |
l
| NTC: (i)           | an AE             | with constraint-consistent |             | reconstruction |             |     |     |     |     |
| ------------------ | ----------------- | -------------------------- | ----------- | -------------- | ----------- | --- | --- | --- | --- |
| for heterogeneous  |                   | flow features,             | and         | (ii) TabCL     | with        |     |     |     |     |
| class-conditioned, |                   | constraint-preserving      |             | augmentations  | and         |     |     |     |     |
| dual-head          | projections       | for feature-type           |             | heterogeneity. | When        |     |     |     |     |
| both branches      | are               | used, their                | predictions | are            | fused by    | a   |     |     |     |
| simple             | confidence/margin | voting                     | rule.       | Because        | such labels |     |     |     |     |
| may be             | noisy, we         | explicitly                 | account for | label noise    | via the     |     |     |     |     |
CLmoduletailoredtoNTCviaper-classquantilethresholds,
| calibration-aware |     | logistic weights, | and | balanced | retention. |     |     |     |     |
| ----------------- | --- | ----------------- | --- | -------- | ---------- | --- | --- | --- | --- |
C
| We then | train | on the | resulting pool | with | confidence- |     |     |     |     |
| ------- | ----- | ------ | -------------- | ---- | ----------- | --- | --- | --- | --- |
final
aware reweighting.
| We adopt      | a closed-world  |                | setting with           | K known    | classes.    |     |     |     |     |
| ------------- | --------------- | -------------- | ---------------------- | ---------- | ----------- | --- | --- | --- | --- |
| Real-world    | NTC             | exhibits class | imbalance              | and        | calibration |     |     |     |     |
| drift across  | classes;        | pseudo-labels  | produced               | by SSL     | contain     |     |     |     |     |
| label noise.  | We assume       | access         | to flow/header-derived |            | fea-        |     |     |     |     |
| tures (no     | deep packet     | inspection     | of                     | payloads). | Our focus   |     |     |     |     |
| is robustness | to label        | scarcity       | and pseudo-label       |            | noise. To   |     |     |     |     |
| maintain      | clarity and     | consistency,   | we                     | define the | notations   |     |     |     |     |
| used in       | Sections III–IV | in Table       | 1.                     |            |             |     |     |     |     |
IV. SELF-SUPERVISEDLEARNINGFOR 5-tuple (source IP, destination IP, source port, destination
PSEUDO-LABELINGANDCONFIDENTLEARNING port, protocol) with idle/active timeouts; time windows
This section first presents a system-level model and data may segment long connections for memory safety. The
flow, from raw packet capture to the unlabeled flow dataset captured flows are then preprocessed to extract features.
| and ultimately | to  | classification. | We then | detail | the tailored |     |     |     |     |
| -------------- | --- | --------------- | ------- | ------ | ------------ | --- | --- | --- | --- |
Thesefeaturescanbebroadlycategorizedintostatistical[11]
SSLtechniques(AEandTabCL)independently,pseudo-label and time-series features [12]. Statistical features include
fusion, and the traffic-adapted CL used to train the final metricssuchasthetotalnumberofpacketsinaflow,thetotal
classifier. bytes transferred, the duration of the flow, and the average
|     |     |     |     |     |     | packet size. | These features | provide a summary | of the flow’s |
| --- | --- | --- | --- | --- | --- | ------------ | -------------- | ----------------- | ------------- |
A. SYSTEMMODELANDEND-TO-ENDDATAFLOW characteristics and can help distinguish between different
Raw packet traces are passively captured at monitored links. types of applications. For example, video streaming appli-
Packets are aggregated into bidirectional flows using the cations might have larger total bytes transferred compared
| VOLUME6,2025 |     |     |     |     |     |     |     |     | 9103 |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | ---- |

ESLAMIANDHAMOUDA:NTCUSINGSSLANDCL
FIGURE1. Pipelinefromrawpackettracestoanunlabeledtraffic-flowfeaturedataset.
FIGURE2. ArchitecturalcomponentsoftrafficclassificationwithSSLandConfidentLearning.
to text-based chat applications. Time-series features, on the As shown in Fig. 2, our framework employs two self-
other hand, capture the temporal patterns in the traffic. contained SSL paths to generate pseudo-labels from D:
l
These can include the inter-arrival times between packets, an AE tailored to tabular flows, which reconstructs hetero-
the distribution of packet sizes over time, or the presence geneous continuous/categorical features; and a TabCL that
of bursty behavior. Such features are particularly useful for performs contrastive pretraining with constraint-preserving
identifying applications with specific timing requirements, view generation and dual-head projections specialized for
such as real-time communications or periodic updates. continuous vs. categorical slices. After SSL pretraining,
Beyond the primary features, we also derive secondary each branch replaces its decoder/projection head with a
featuresbysimpleaggregationsandratios(e.g.,mean/variance classifier and is fine-tuned on the small labeled set D
s
of inter-arrival time (IAT), byte/packet rates, up/down (freeze–unfreeze). Each branch can independently pro-
throughput,andburst-lengthratios),whichenrichthetabular duce pseudo-labels via its fine-tuned classifier. Using two
representation without accessing payloads. In addition to SSL methods is advantageous because the AE branch is
these numeric attributes, there are categorical features such reconstruction-driven and encourages feature-wise consis-
as protocol and flow direction. The categorical fields are tency and simple algebraic relations, whereas the TabCL
encoded as one-hot or embeddings, while numeric fields branch is discrimination-driven and emphasizes class-
arestandardized/normalized.Thisproducesalargeunlabeled consistentinvarianceswhilerespectingheterogeneitythrough
traffic-flow dataset D; a small labeled subset D is curated its dual heads, potentially capturing complementary traffic
l s
via DPI/heuristics/manual checks and used only for fine- patterns. When both are available, their predictions can
tuningandmodelselection.Thepipelineofunlabeleddataset be combined using a confidence-margin voting rule to
generation from raw network packets is illustrated in Fig. 1. enhancepseudo-labelquality;alternatively,thesingle-branch
9104 VOLUME6,2025

output is used. Following SSL, a traffic-adapted CL module such tuples, encouraging these relations to hold improves
estimates label noise on the pseudo-labeled pool, regardless plausibility and stabilizes the latent representation. We
of whether it came from AE, TabCL, or their fusion. It uses formalize this with a set of algebraic residuals applied to
out-of-sample probabilities, builds the confident joint, and the reconstructed continuous vector(cid:2)x :
cont
(cid:9) (cid:10)
assigns per-sample training weights via per-class quantile
G = g : Rdcont →R | m=1,...,|G| ,
thresholds with calibration-aware smoothing and balanced m
retention.ThefinalclassifierC final istrainedontheweighted where each g m ((cid:2)x cont ) is the residual of constraint m when
pseudo-labeled set using symmetric cross-entropy loss. This evaluated on the reconstructed continuous vector. We then
overviewsetsthestage;detaileddescriptions,algorithms,and define
mathematical formulas for NTC-aware AE, TabCL, fusion, (cid:11)|G| (cid:12) (cid:3) (cid:4)(cid:12)
and CL follow in the next separate subsections. L = φ (cid:12) g (cid:2)x (cid:12) , (2)
cons m m cont 1
m=1
B. AUTOENCODER-BASEDSELF-SUPERVISED where φ >0 are modest weights. This penalty nudges the
m
LEARNING
encoder and decoder to reconstruct plausible tuples without
An AE learns a compressed representation of the input
prescribing any particular feature identity, and improves the
data by encoding it into a lower-dimensional latent space
semantic quality of the representation reused at fine-tuning
and reconstructing it, capturing underlying patterns in an
time.
unsupervised manner. We represent each network flow as
a feature vector x ∈ Rd comprising two types of attributes
2) FINE-TUNINGANDPSEUDO-LABELING
that are typical of network-traffic data: (i) continuous,
After pretraining on D with (1), the decoder is replaced
l
numeric features (e.g., counts, durations, or rates) denoted
by a classifier C(·;θ C ) attached to the encoder. We adopt a
by x , and (ii) categorical features (e.g., protocol, flow
cont short freeze–unfreeze schedule. This schedule is a standard
direction) denoted collectively by x . Categorical attributes
cat practice that reduces optimization drift when transplanting a
are encoded in standard numeric form (e.g., one-hot or
new head on a pretrained encoder. First, we freeze θ E and
embeddings) and are reconstructed with a cross-entropy
optimize θ C on D s to stabilize the new head, then jointly
objective. This heterogeneous structure is characteristic of
unfreeze (θ E ,θ C ) and fine-tune on D s with the standard
tabular network-flow representations and motivates losses
cross-entropy:
that respect both numeric reconstruction fidelity and cate- (cid:11) (cid:13) (cid:3) (cid:4) (cid:14)
1
gorical consistency. We utilize an AE to first learn latent L = − log C E(x) [y] . (3)
representations from D l and second, generate pseudo-labels,
CE |D
s
|
(x,y)∈Ds
subsequently fine-tuning with D . This AE branch is self-
s After fine-tuning, we apply the trained head to all x ∈ D
contained and can be used on its own to produce the l
and assign pseudo-labels by top-1 prediction.
pseudo-labeled pool for the downstream CL stage.
3) HYPERPARAMETERSELECTION
1) PRETRAININGOBJECTIVEWITH
CONSTRAINT-CONSISTENTRECONSTRUCTION Latent width, learning rates, the freeze duration, and the
Let E(x;θ E ) be the encoder and D(h,;θ D ) the decoder. coefficients {φ m } in (2) are chosen by stratified cross-
Given an input x, the model produces a latent code h = validation on D s , targeting macro-F1 after fine-tuning. This
E(x) and a reconstruction (cid:2)x = D(h), with corresponding keeps the added constraint term modest and data-adaptive,
splits(cid:2)x and(cid:2)x . The pretraining loss function combines avoiding over-regularization on classes whose statistics
cont cat
a mixed reconstruction term with a small, domain-consistent naturally vary. Algorithm 1 summarizes the procedure.
penaltythatsoftlyenforcessimplealgebraicrelationsamong
selected continuous coordinates: C. TABULARCONTRASTIVELEARNING(TABCL)
(cid:3) (cid:4) (cid:3) (cid:4)
TabCL offers an alternative SSL approach by learning
L = MSE x ,(cid:2)x +CE x ,(cid:2)x + L ,
AE (cid:5) cont cont(cid:6)(cid:7) cat cat cat(cid:8) (cid:5)(cid:6)co(cid:7)n(cid:8)s invariant representations through contrastive loss, enhancing
mixedreconstruction constraint the model’s ability to generalize across diverse traffic
consistency
flows. TabCL leverages contrastive learning to maximize
(1)
the similarity between augmented versions of the same data
where MSE is the mean squared error on continuous sample (positive pairs) while distinguishing it from others
features, and CE denotes the sum of cross-entropy terms (negative pairs), making it particularly effective for tabular
over all categorical fields (each field modeled with an data. The detailed workflow of TabCL method is presented
appropriate softmax). In network-traffic data, several con- in Fig. 3. We adopt the standard two-view NT-Xent setup
tinuous attributes are related by simple algebra (e.g., a and tailor it to network-traffic data with two components:
rate-like feature equals a bytes-like feature over a duration- a class-conditioned replacement scheme to create views,
like feature; a packet-length-like feature equals the sum of and a constraint-preserving projection that enforces sim-
payload-andheader-likefeatures).WhentheAEreconstructs ple identities among reconstructed continuous attributes in
VOLUME6,2025 9105

ESLAMIANDHAMOUDA:NTCUSINGSSLANDCL
Algorithm 1 Autoencoder-SSL With Constraint-Consistent Refreshing stops after a small number of rounds or once the
Reconstruction fraction of changed labels falls below a tolerance.
Require: Unlabeled D l , labeled D s , batch size m, learning For each anchor x with current class identity c = y˜(t) ,
rate η we create two views i (cid:15)x (1) and (cid:15)x (2) by replacing i a sm i all
1: Initialize encoder E(·;θ E ), decoder D(·;θ D ) subset of the anchor’s f i eatures. L i et d denote the number
2: PretrainonD l : of features (coordinates) of x, and let r ∈ (0,1) be the
3: for epoch =1,2,... do i
replacement rate. In each view, we randomly select exactly
4: for mini-batch {x i }m i=1 ⊂D l do (cid:8)rd(cid:9) features of the anchor to replace. Denote by I(t) ⊂
5: z i ←E(x i ); (cid:2)x i ←D(z i ) {1,...,d} the index set chosen for view t ∈ {1,2}; the
6: ComputeL AE from(1)withL cons in(2)(weights twosetsaresampledindependently(preferablywithminimal
φ m ); update (θ E ,θ D )←(θ E ,θ D )−η∇L AE . overlap). For every index j ∈ I(t) , the new value is drawn
7: Replace D by classifier C(·;θ C ) from the empirical distribution of the same feature among
8: Freeze θ E; train θ C on D s using CE (3) flows currently labeled c i , while all other features are kept
9: Unfreeze (θ E ,θ C ); joint fine-tuning on D s with (3) equal to the anchor:
10: Pseudo-labeling: for all x ∈ D l , set (cid:2)c ← (cid:3) (cid:4)
Ensu ar r g e: m P ax se k u C d ( o E - ( l x ab )) e [ l k e ] d D l ={(x,(cid:2)c)} (cid:15)x (cid:15)x ( ( i t t ) ) [ [ k j ] ] ∼ = P x[ x k [ ] j , ] k | ∈/ y˜ = I(t c ). i ,j∈I(t), ( ( 4 5 ) )
i i
This class-conditioned replacement (TabCL principle) keeps
views semantically close to the anchor x while inducing
i
invariances within the class manifold.
After replacement, we update each view to satisfy simple
algebraic identities among continuous features, using the
residual set G defined in the AE subsection. In practice,
we adjust the augmented vector only as much as needed to
restore identities (e.g., “rate = bytes / duration” or “packet
length = payload + header”), keeping the view close to
the original replacement outcome while making the tuple
plausibleintermsofinter-featureconsistency.Letx˘(t)
denote
i
the adjusted view:
(cid:3) (cid:4)
x˘(t) = (cid:5) G (cid:15)x (t) , (6)
i i (cid:12) (cid:12)
(cid:2) argmin (cid:12) u−(cid:15)x (t)(cid:12)2
u(cid:3) (cid:4) i 2
s.t. g u =0, ∀g ∈G.
m cont m
Here, u is the optimization variable (the adjusted vector
we solve for), u cont is its continuous slice, (cid:5) G (.) denotes
the projection operator that returns the nearest vector that
satisfies all constraints in G, and argmin selects the point
FIGURE3. WorkflowofTabCLforpseudo-labeling.
that minimizes the squared distance to the replaced view.
This constraint-preserving update is simple (closed-form
network traffic datasets. In addition, we use a dual-head or single-pass updates for ratio/product/sum identities) and
contrastive objective to accommodate heterogeneous feature ensures that positives are plausible flow tuples. Although
types with distinct temperature scales. This TabCL branch applied at the view level, the induced gradients during pre-
is independent of AE and can be run alone to generate the training bias the encoder’s representation toward respecting
pseudo-labeled pool. such identities, which we later reuse for supervised fine-
tuning.
1) TWO-VIEWAUGMENTATIONSFORTABULARFLOWS
BeforepretraininginTabCL,wefirstobtainprimarypseudo- 2) DUAL-HEADPROJECTIONSFORHETEROGENEOUS
labels
{y˜(0)}
for D by training a light classifier on D and
FEATURES
i l s
applyingittoD l .Duringcontrastivepretraining,weperiodi- After creating two augmented views by class-conditioned
cally refresh these pseudo-labels: at predefined intervals, we replacement and constraint-preserving update, in the pre-
freeze the current encoder E, train a fresh linear probe on trainingphase,weadopttheNormalizedTemperature-scaled
{E(x),y} (x,y)∈Ds , and reclassify {E(x)} x∈Dl to obtain {y˜(
i
t)}. Cross-Entropy (NT-Xent) loss, which promotes similarity
9106 VOLUME6,2025

between augmented views. For projection vectors v,v and Algorithm2 TabCL With Class-Conditioned Replacement,
i j
temperature τ >0, the NT-Xent term is: Constraint Projection, and Dual-Head Objective
(cid:16) (cid:3) (cid:4) (cid:18)
Require: Unlabeled D, labeled D ; replacement rate r;
L NT-Xent (cid:3) v i ,v j ,τ (cid:4) =−log (cid:17) k e (cid:12)= x i p ex s p im (s ( im v i , (v v i j , )/ v τ k )/τ) .(7) 1: r B e o fr o e t s s h tr i a n p te : r t v ra a i l n ; t a em li l g p h e t ra c t l u a r s e s s ifi τ e c r o s n o t n ,τ D ca s t ; ; g m e i t x i i n n i g tia λ l{y˜( i 0)}
Here, sim(v,v) denotes the cosine similarity between the for D l
projection ve i cto j rs: 2: Initialize encoder E and projectors P cont ,P cat
(cid:3) (cid:4) v ·v 3: for epoch =1,2,... do
sim v i ,v j = |v i ||v j | . (8) 4: if refresh interval reached then
For each mini-batch containing N i a j nchors, we form two 5: reclassif F y ree { z E e (x E ) ; } trai t n o a o l b in ta e i a n r p { r y˜ o (t b )} e ; o s n to { p (E( re x f ) r , e y s ) h } i D n s g ;
Dl i
augmented views per anchor and each view is encoded by if label-change fraction < tolerance or max rounds
the shared backbone and then mapped by two independent reached.
p t p h r r e o o j j e e e m c c t t b i o o e r n dd P h i c n e o a g n d t z s ( i t t o t ) a = il o o b E r t e ( a d x˘ in ( i t t ) o ) v , ( c t f t h o ) e n e e t, d i fe i a = t t t u o r P e a c t c o y n o p t n ( e z t s i ( i n : t) u ) w o , u e a s c - n f o d o m cu t p o s u e t d e a 6 7 : : I(1) f , o I r ( F 2 m ) o i r o n f i e -b s a i a c z t h e ch (cid:8) i: r { d x s (cid:9) i e } t N i= c 1 i ⊂ ← D l y˜ d ( i t o ) ; sample index sets
categorical-focusedprojectorP cat toobtainv ( c t a ) t,i =P cat (z ( i t)) 8: For t ∈ {1,2}: replace (cid:15)x ( i t) [j] ∼ P(x[j] | y˜ =
for t ∈ {1,2} and i = 1,...,N. Each anchor, therefore, c) for j ∈ I(t) , copy others from x; then project to
i i
appears twice (once per view) as the “query,” and for each constraints x˘(t) ←(cid:5) G ((cid:15)x (t)) as in (6).
i i
queryweuseitscounterpartviewasthepositiveandallother 9: Encode/project: z ( i t) ← E(x˘( i t)); v ( c t o ) nt,i ←
in-batchprojectedviewsfromthesameheadasnegatives.To P (z (t)); v (t) ←P (z (t))
preserve symmetry, we evaluate NT-Xent in both directions cont i cat,i cat i
(view 1 as anchor with view 2 as positive, and vice versa) 10: Compute L cont and L cat via (9), (10)
and average across the resulting 2N anchorings per head. 11: Compute L TabCL =λL cont +(1−λ)L cat (11); update
parameters
The head-specific losses are thus
(cid:11)N (cid:19) (cid:3) (cid:4) 12: Discard projectors; attach C to E; fine-tune on D s with
L = 1 L v (1) ,v (2) ,τ (3); pseudo-label D l
cont
2N
NT-Xent cont,i cont,i cont
Ensure: Pseudo-labeled D from TabCL
i=1 (cid:3) (cid:4)(cid:20) l
+ L v (2) ,v (1) ,τ . (9)
NT-Xent cont,i cont,i cont
(cid:11)N (cid:19) (cid:3) (cid:4) freeze–unfreezescheduleandcross-entropy(cf.Eq.(3)).We
L cat = 2 1 N L NT-Xent v ( c 1 a ) t,i ,v ( c 2 a ) t,i ,τ cat then apply C◦E to all x∈D l to obtain final pseudo-labels.
i=1 (cid:3) (cid:4)(cid:20) The hyperparameters such as temperatures (τ cat ,τ cont ), the
+ L v (2) ,v (1) ,τ . (10) mixing coefficient λ, the replacement rate r, and the refresh
NT-Xent cat,i cat,i cat
schedule are selected on D via stratified cross-validation
s
The overall contrastive objective combines the two heads to maximize macro-F1 after fine-tuning. Algorithm 2 details
with a convex weight: the expanded procedure.
L = λL + (1−λ)L , λ∈[0,1]. (11)
TabCL cont cat
D. FUSIONOFAEANDTABCLPSEUDO-LABELS
In our framework, instead of a single projection head with
Either SSL branch (AE or TabCL) can independently be
a single temperature shared across all features, we employ
used to produce a pseudo-labeled pool for the subsequent
dual-head projections with head-specific temperatures. This
CLstage.Whenbothareavailable,weadoptasimplevoting
design acknowledges that network-flow tables are heteroge-
rulethatconsolidatestheirpredictionsatnegligibleoverhead.
neous features.
For each flow x, let
Using distinct temperatures is beneficial because categor-
ical similarities are typically sharper (best handled with a (cid:2)cAE(x)=arg max pAE(x), (12)
smaller τ ), while continuous similarities are more variable k∈{1,...,K} k
cat
(more stable with a larger τ cont ). The shared encoder thus (cid:2)cTabCL(x)=arg k∈{ m 1, a .. x .,K} pT k abCL(x), (13)
learnsrepresentationsthataresimultaneouslyrobustforboth
feature types, while each head specializes its geometry (via be the top-1 classes predicted by the AE and TabCL
temperature) to the statistics of its slice. classifiers, where pAE(x),pTabCL(x) ∈ [0,1]K are their
respectivesoftmaxprobabilityvectors.Definetheconfidence
3) FINE-TUNING,PSEUDO-LABELING,AND of each branch as its top-1 probability,
HYPERPARAMETERS
sAE(x) = max pAE(x), sTabCL(x) = max pTabCL(x),
After contrastive pretraining, we discard P cont and P cat , k k k k
attachaclassifierC(·;θ C )toE,andfine-tuneonD s usingthe (14)
VOLUME6,2025 9107

ESLAMIANDHAMOUDA:NTCUSINGSSLANDCL
Algorithm3 Confidence–Margin Voting Fusion of AE and Algorithm4 Traffic-Adapted CL With Quantile Thresholds,
TabCL Logistic Weights, BRC, and Weighted SCE
Require: Trained AE and TabCL classifiers; unlabeled D l Require: Pseudo-labeled D l = {(x i ,y˜ i )}; small labeled D s ;
Ensure: Fused pseudo-labels on D l folds F; grids Q (quantile q), W (w min ), (cid:8) (slope γ)
1: for each x∈D l do Ensure: Trained final classifier C final
2:
pAE ←softmaxfromAE; pTabCL ←softmaxfrom
1: Out-of-sample probabilities: obtain p i via F-fold CV
TabCL (18); set s ←p[y˜ ] (19)
i i i
3: (cid:2)cAE ← argmax k pAE[k]; (cid:2)cTabCL ← 2: Thresholds/weightsperclass:
argmax k pTabCL[k] (12) 3: for q∈Q, w min ∈W, γ ∈(cid:8) do
4: if(cid:2)cAE =(cid:2)cTabCL then 4: for each class j do
5: (cid:2)c←(cid:2)cAE 5: Compute t j (q) (20), m˜ j (21), MAD j (22), σ j (23)
6: else
7 8 : : ( s 1 Ta 4 b ) CL− s m A A m E E a ← x ← k(cid:12)= m (cid:2)cT a a s b x A C k L E p p − A T E ab [ m C k L ] a ; x [k k ] (cid:12)= s (cid:2)c T ( A 1 a E b 5 C ) p L AE ← [k] m ; ax m k T p a T b a C b L CL[ ← k] 6 7 8 9 : : : : f B o u r il z w e d i a i ← c c ← h on ( i w f s i d i d m o − e in n t t + y ( ˜ q i j ) o ( ) 1 i / n ( − t γ (cid:2) Q w σ y˜ m i ( ) i 2 n 7 ) (2 ) · ; 4 s ) g ig e m t ( ρ z j i ) (2 (2 8 6 ); ) compute
9: Decide(cid:2)c by rule (17): prefer higher confidence; a j (29)
if tied, prefer larger margin; fall back deterministically 10: Final weights: w (cid:15) i ← clip(a j w i , w min , 1) (30) for
y˜ =j
otherwise. i
10: Assign(cid:2)c to x 11: Train C final on D l with weighted SCE (31)
12: Deployment: fix (q,w min ,γ) according to the
chosen configuration; recompute {w (cid:15)} on the full
i
pseudo-labeled pool and train C on D.
and the margin (gap between the highest and the second- final l
highest probabilities),
mAE(x) = sAE(x) − max pAE(x), (15)
k(cid:12)=(cid:2)cAE k performance. We aim to reduce the impact of noisy pseudo-
mTabCL(x) = sTabCL(x) − max pTabCL(x). (16) labels before training the final classifier. We therefore adopt
k
k(cid:12)=(cid:2)cTabCL and extend CL [26] into a pipeline that down-weights
The fused pseudo-label(cid:2)c(x) is decided by agreement, then noisy pseudo-labels and trains the final classifier in five
stages: First, following standard CL practice, we compute
by confidence, then by margin:
⎧ out-of-sample prediction probabilities and define each sam-
⎪⎪⎪⎪⎪⎪⎨
(cid:2)
(cid:2)
c
cA
A
E
E
(
(
x
x
)
)
i
i
f
f
(cid:2)c
sA
A
E
E
(
(
x
x
)
)
>
=(cid:2)
s
c
T
T
a
a
b
b
C
C
L
L
(
(
x
x
)
)
,
, p
q
l
u
e
a
’
n
s
ti
s
l
e
e
l
-
f
b
-
a
c
s
o
e
n
d
fid
c
e
o
n
n
c
fi
e
d
.
en
S
c
e
e
co
t
n
h
d
re
,
s
w
ho
e
ld
i
s
nt
w
ro
i
d
th
uc
r
e
ob
c
u
l
s
a
t
ss
d
-
i
a
s
d
p
a
e
p
r
t
s
i
i
v
o
e
n
,
(cid:2)cTabCL(x)if sTabCL(x)>sAE(x), (MAD) to reflect per-class difficulty. Third, we convert
(cid:2)c(x) = (17)
⎪⎪⎪⎪⎪⎪⎩
(cid:2)cAE(x)
i
a
f
nd
sA
m
E(
A
x
E
)
(
=
x)
s
≥
Tab
m
C
T
L
a
(
b
x
C
)
L(x)
c
ti
o
c
nf
w
id
e
e
i
n
g
c
h
e
ts
in
t
t
h
o
at
sm
a
o
tt
o
e
t
n
h
u
,
a
c
t
a
e
lib
u
r
n
a
c
ti
e
o
r
n
ta
-
i
a
n
wa
p
r
s
e
e
p
u
e
d
r
o
-
-
s
l
a
a
m
be
p
l
l
s
e l
w
og
h
i
i
s
le
-
(cid:2)cTabCL(x)otherwise. retaining all data. Fourth, leveraging the CL confident
joint, we perform a class-wise balanced retention calibration
This rule favors the model with the higher top-1 confidence;
that aligns each class’s retained mass with its estimated
ifconfidencestieexactly,thelargermargin(sharperdecision)
clean fraction, mitigating imbalance under label noise.
prevails. In practice, exact ties are exceedingly rare; the last
Finally, we train the final classifier C using weighted
line provides a deterministic fallback. The resulting single final
symmetric cross-entropy on the full pseudo-labeled set.
pseudo-labeled set is then passed to the downstream task.
Importantly, we do not remove samples; rather, we reduce
The process of fusion is detailed in Algorithm 3.
the contribution of uncertain ones and calibrate class masses
Fusion often improves corner cases where the two
to stabilize learning. The complete CL-driven noise mitiga-
branches disagree on difficult classes, with minimal changes
tion and downstream training procedure is summarized in
to the pipeline. The cost is additional SSL pretraining
Algorithm 4.
(both branches), which we report explicitly in the efficiency
section, together with parameter counts and epochs for each
path. 1) PREDICTIONPROBABILITIESAND
SELF-CONFIDENCE
E. CONFIDENTLEARNINGFORNOISEREDUCTIONAND We first obtain out-of-sample predicted probabilities p i for
FINALCLASSIFICATION each sample x i in D l using F-fold cross-validation with a
The pseudo-labeled pool D = {(x,y˜ )}|Dl | produced by simple classifier (a shallow MLP), for each sample x, use
l i i i=1 i
SSL, as detailed in the preceding subsections, inevitably the model trained on the F−1 folds that did not include
contains noise. Training directly on these labels degrades x. Denoting the parameters of this model by
θ(−f(i))
, we
i
9108 VOLUME6,2025

calculate the K-way probability vector: threshold and on the dispersion of confidences in that class.
(cid:25) (cid:3) (cid:4) (cid:3) (cid:4)(cid:26) For each observed class, we define the class median by:
p i = P y=1|x i ;θ(−f(i)) , ...,P y=K |x i ;θ(−f(i)) , (cid:3) (cid:4)
(cid:11)K m˜ j = median S j . (21)
p ∈[0,1]K, p[k]=1. (18)
i i
WemeasuredispersionusingtheMedianAbsoluteDeviation
k=1
(MAD):
In other words, p i is P(y | x i ) evaluated for all classes. (cid:9) (cid:10)
The top-1 class of this out-of-sample model is yˆ(cid:12) i = MAD j = median |s−m˜ j |:s∈S j . (22)
argmax p[k],whichmayormaynotequaltheSSLpseudo-
label y˜ . k In i CL, the quantity of interest is self-confidence We set the classwise scale to σ j and clip it to avoid division
i
by zero:
s, defined as the probability that the out-of-sample model
i
(cid:3) (cid:4)
assigns to the observed (pseudo) label of the sample: σ ← max MAD,ε , ε >0. (23)
(cid:25) (cid:26) j j
s = p y˜ ∈ [0,1]. (19)
i i i Using MAD makes the scale estimate robust to outliers and
Thus, p i is a K-dimensional probability vector (P(y | x i ) skewed score distributions commo (q n ) in traffic flows. Given
the per-class quantile threshold t from (20), define for
v ac e r c o to ss r c a o ll rr c e l s a p s o se n s d ) i , ng wh to ile y˜ s . i T i h s e a se s o in u g t- le of s -s c a a m la p r le en p tr r y ed o ic f ti t o h n a s t sample i with y˜ i =j: j
i
andtheresultingself-confidencesareusedexclusivelytovet s −t (q)
pseudo-labelsviaCL;theydonotprovidegradientstoC final . z i = i γ σ y˜ i , (24)
y˜
i
2) PER-CLASS,QUANTILE-CALIBRATEDTHRESHOLDS where γ > 0 controls the slope around the threshold. We
For each observed class j ∈ {1,...,K}, collect the self- map z to (0,1) with the logistic function that is:
i
confidence scores of samples whose pseudo-label equals j:
1
S
no
j
n
=
-d
{
ec
s i
re
:
as
y˜
i
i
n
=
g o
j}
rd
,
e
a
r
nd
be
n j
s j
=
,(1)
|S
≤
j |.
s
L
j,(
e
2
t
)
t
≤
he
·
e
·
l
·
e
≤
me
s
n
j,
t
(
s
nj
o
)
f
(o
S
r
j
de
in
r
sigm(z i ) = 1+e−zi . (25)
statistics).Foraquantilelevelq∈(0,1],definetheper-class With a minimum weight w ∈ (0,1), the per-sample
min
q-quantile threshold by the standard order-statistic rule: training weight is:
(cid:3) (cid:4)
t j (q) = Q (cid:27) uan (cid:28) tile q S j (cid:2) s j,( kj (q)) , w i = w min + (1−w min )·sigm(z i ) ∈ [w min , 1]. (26)
k j (q) = qn j , q∈(0,1]. (20) All hyperparameters in (23)–(26) (e.g., w , γ, ε) are
min
(q) selected via stratified cross-validation on the small labeled
(Equivalently, t is the smallest value for which at least a
j set D .
fraction q of the scores in S j are ≤t j (q) ; linear interpolation The s weighting mechanism in (26) behaves in a stable
can be used if a specific quantile convention is desired.) and interpretable manner. By construction w ∈ [w ,1];
i min
We treat q as a hyperparameter shared across classes and When s (cid:17)t (q) , the pseudo-label of the flow is likely noisy,
select it by stratified cross-validation on the small labeled the stan
i
dardi
y˜
z i ed margin z → −∞ and thus w → w .
i i min
set D s . This procedure ties the threshold choice directly Conversely,whens (cid:19)t (q) ,thepseudo-labelislikelycorrect,
t
a
o
da C
d
p a
o
t n i
w
v o i
n
n t
s
y i
t
c
r
a o
e
l f
am
C t j
(
L
q) p
[ .
e
2
r
6
fo
]
r
u
m
se
a
s
nc
th
e
e
w
pe
h
r
i
-
l
c
e
la
p
s
r
s
es
m
e
e
rv
a
i
n
ng
sel
t
f
h
-
e
co
p
n
e
fi
r
d
-c
e
l
n
a
c
s
e
s z
z i i =
→
0
+
a
∞
nd w
an
i
d
=
w
w i m
i →
in +
1 y . ˜
1 2
i
(
A
1
t
−
th
w
e
m
t
in
h
)
r
,
es
i.
h
e
o
.,
ld
t
,
he
if
ex
s
i ac
=
t m
t
y
(
˜
q
i i d
)
p
t
o
h
i
e
n
n
t
as a threshold t (mean) = S ¯ . In contrast, we set the class between the minimum and maximum weights.
j j
thresholdtoaquantileofS,whichofferstwoadvantagesfor
j
network traffic flows: (i) it adapts to class-dependent score 4) CONFIDENTJOINTANDCLASS-WISEBALANCED
distributions that are often skewed due to heterogeneous RETENTION
or encrypted traffic patterns, making the cutoff robust to In CL, the matrix (cid:2) Q ∈ RK×K summarizes the estimated
outliers; and (ii) it provides an explicit strictness control via joint between the latent true class (rows) and the pseudo-
q: higher q yields a stricter threshold (fewer samples lie label (columns). It is computed directly from out-of-sample
above t j
(q)
and will later receive large weights), while lower probability vectors p i using soft counts. Specifically,
q is more permissive. (cid:11)
(cid:2) Q y=k,y˜=j = p i [k], k,j∈{1,...,K}, (27)
3) CALIBRATION-AWAREPER-SAMPLEWEIGHTS
i:y˜
i
=j
To avoid hard pruning (outright removal of suspected-noisy wheretherowindex“y=k”denotesthelatentclassinferred
(cid:2)
samples)andtostabilizetraining,wedefineasmoothweight from p i . The diagonal entry Q j,j e(cid:17)stimates the clean mass
(cid:2)
for each sample that depends on its distance to the class for class j, while the column sum k Q k,j is the total mass
VOLUME6,2025 9109

ESLAMIANDHAMOUDA:NTCUSINGSSLANDCL
Then,parametersofC
observed as j. The corresponding estimated clean fraction areupdatedbygradientdescent:
final
| for observed | class | j is: |         |     |     |     |     |     |       |     |       |       |     |        |
| ------------ | ----- | ----- | ------- | --- | --- | --- | --- | --- | ----- | --- | ----- | ----- | --- | ------ |
|              |       |       |         |     |     |     |     |     | θ     | ←   | θ     | − η∇  | L   | . (34) |
|              |       |       |         |     |     |     |     |     | final |     | final | θ     | SCE |        |
|              |       |       | (cid:2) |     |     |     |     |     |       |     |       | final |     |        |
Q j ,j
ρ = (cid:17) ∈ [0,1]. (28) Buildingonthemathematicalformulationsandprocedural
|     |     | j   | (cid:2) |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Q k,j details outlined above, our innovations make this foundation
k
To mitigate minority erosion under class imbalance, a more suitable for the unique challenges of network traffic.
Balanced Retention Constraint (BRC) is applied after com- Unlike original CL, which relies on mean-based thresholds
|     |     |     |     |     | (cid:2) | #{i | y˜ = j}, |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
puting per-sample weights w i . Define n j : i that can be sensitive to skewed confidence distributions
the tar(cid:17)get effective mass T (cid:2) ρ N , and the current mass common in imbalanced and heterogeneous traffic data, our
|     |     |     | j   | j j |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
M (cid:2) w . The classwise scaling factor is: quantile-calibrated thresholds provide a more robust cutoff
| j   | i:y˜ =j i |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i
|     |     |     |     |     |     |     |     | by adapting | to  | class-specific |     | variation | and | outliers; this |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | -------------- | --- | --------- | --- | -------------- |
T
a = (cid:3) j (cid:4), (29) avoids overly strict filtering for hard classes and overly lax
|     |     | j   |     | (cid:14), |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | max | M         | j   |     |     |     |     |     |     |     |     |     |
filteringforeasyones.Similarly,whilethecanonicalmethod
where (cid:14) > 0 provides numerical stability. The final per- often uses hard pruning that risks losing valuable samples,
|        |             |     |          |          |         |     |     | our logistic | weights |     | enable | nuanced | attenuation, | retaining |
| ------ | ----------- | --- | -------- | -------- | ------- | --- | --- | ------------ | ------- | --- | ------ | ------- | ------------ | --------- |
| sample | weight used | in  | training | is then: |         |     |     |              |         |     |        |         |              |           |
|        |             |     | (cid:3)  |          | (cid:4) |     |     |              |         |     |        |         |              |           |
(cid:15) partial contributions from uncertain instances to preserve
|     | w   | =   | clip a | w, w | , 1 , |     | (30) |     |     |     |     |     |     |     |
| --- | --- | --- | ------ | ---- | ----- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
i j i min information and maintain dataset richness. Furthermore, the
(cid:17)
(cid:15) ≈
This soft constraint yields i:y˜ =j w T j (within a small balanced retention mechanism addresses class imbalance by
|     |     |     |     | i   | i   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tolerance), aligning the retained mass of each observed class scaling masses according to clean estimates, a step not
|          |                |     |           |      |            |     |     | present | in the | original | that | helps preserve |     | minority flows. |
| -------- | -------------- | --- | --------- | ---- | ---------- | --- | --- | ------- | ------ | -------- | ---- | -------------- | --- | --------------- |
| with its | clean fraction |     | estimated | from | (27)–(28). |     |     |         |        |          |      |                |     |                 |
|          | <              |     | >         |      |            |     |     |         |        |          |      |                |     |                 |
If M T, then a 1 and all weights in class j Together, these enhancements make our module more effec-
| j   | j   |     | j   |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
are uniformly lifted (subject to clipping), preventing under- tive for traffic classification, where class skew and variable
|     |     |     |     |     | >T, |     | <1  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
retention of harder/minority classes; if M j j then a j noise are prevalent. Beyond this intuition, our ablations and
and the class is gently down-scaled to avoid over-retention. experiments across different datasets (Section V) confirm
w ∈ [w ,1], thatthistraffic-adaptedCLoutperformstheoriginalapproach
| Because | i   | min | the | effective | mass | per class | lies | in  |     |     |     |     |     |     |
| ------- | --- | --- | --- | --------- | ---- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- |
| n,      |     |     |     |           |      | = ρN,     |      |     |     |     |     |     |     |     |
[w n]; the BRC moves it toward T thereby in terms of overall classification performance.
| min j        | j        |         |              |            | j            | j j             |     |                       |     |     |     |     |     |     |
| ------------ | -------- | ------- | ------------ | ---------- | ------------ | --------------- | --- | --------------------- | --- | --- | --- | --- | --- | --- |
| preserving   | minority | classes | in           | proportion | to           | their estimated |     |                       |     |     |     |     |     |     |
|              |          |         |              |            |              |                 |     | V. EVALUATION&RESULTS |     |     |     |     |     |     |
| cleanliness. | Equation |         | (27) follows |            | the standard | confident       |     |                       |     |     |     |     |     |     |
joint construction in CL [26], whereas the scaling rule The evaluation of the proposed NTC model is presented in
in (29) and (30) constitutes the proposed extension that this section, with the objective of assessing its performance.
|                                 |     |             |           |     |        |           |     | The aim      | is to | compare    | the       | model’s effectiveness |     | using key      |
| ------------------------------- | --- | ----------- | --------- | --- | ------ | --------- | --- | ------------ | ----- | ---------- | --------- | --------------------- | --- | -------------- |
| operationalizes                 |     | class-aware | retention |     | during | training. |     |              |       |            |           |                       |     |                |
|                                 |     |             |           |     |        |           |     | metrics such | as    | precision, | F1-score, | recall,               | and | classification |
| 5) FINALTRAININGWITHWEIGHTEDSCE |     |             |           |     |        |           |     | accuracy.    |       |            |           |                       |     |                |
C
| The downstream |     | classifier |     | is  | trained | on the | pseudo- |     |     |     |     |     |     |     |
| -------------- | --- | ---------- | --- | --- | ------- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- |
final
labeled dataset D = {(x,y˜ )} using the Symmetric A. SIMULATIONSETTINGANDDATASETS
|     |     | l   |     | i i |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Cross-Entropy (SCE) loss, weighted by the final per-sample To assess the proposed model, we utilized two distinct
(cid:15)
weight w from (30). For a sample (x,y˜ ) with predicted datasets: a self-generated dataset treated as unlabeled for
|     | i   |     |     |     | i i |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
probability vector p =C (x)∈[0,1]K, the loss is: SSL and a small labeled dataset derived from the ISCX
|     |     | i        | final | i   |     |          |     |     |     |     |     |     |     |     |
| --- | --- | -------- | ----- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | (cid:25) |       |     |     | (cid:26) |     |     |     |     |     |     |     |     |
L(i) (cid:15) VPN-nonVPNdataset[12].Weusedaself-generateddataset
|     | (cid:2) | w αCE(p,y˜ |     | ) + | βRCE(y˜ | ,p) | . (31) |     |     |     |     |     |     |     |
| --- | ------- | ---------- | --- | --- | ------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
SCE i i i i i to demonstrate the full, deployment-style pipeline from raw
α,β > packet capture to flow-level tabular features under realistic
| The coefficients |     |     | 0   | are hyperparameters |     |     | and are |     |     |     |     |     |     |     |
| ---------------- | --- | --- | --- | ------------------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
selectedbystratifiedcross-validationonthesmalllabeledset label scarcity and class imbalance. In addition to these
datasets,wealsoevaluateontheUCDavis-QUIC[40]dataset
| D s . We | adopt SCE | because |     | it combines | the | standard | cross- |     |     |     |     |     |     |     |
| -------- | --------- | ------- | --- | ----------- | --- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- |
entropy (encouraging correct predictions) with a reverse tobroadentheevaluationandassessgeneralizationtomodern
cross-entropy term that penalizes overconfident mistakes, encrypted traffic. Below, we describe each dataset in detail,
|           |                   |          |             |          |       |          |         | including          | how | it was  | created, | its characteristics, |     | and its role |
| --------- | ----------------- | -------- | ----------- | -------- | ----- | -------- | ------- | ------------------ | --- | ------- | -------- | -------------------- | --- | ------------ |
| improving | robustness        |          | under       | residual | label | noise in | pseudo- |                    |     |         |          |                      |     |              |
| labeled   | data. Concretely, |          |             |          |       |          |         | in the evaluation. |     |         |          |                      |     |              |
|           |                   | (cid:29) |             |          |       |          |         | Self-Generated     |     | Dataset |          | as an Unlabeled:     |     | The large    |
|           |                   |          | 1−(cid:14), | k=y˜     | ,     |          |         |                    |     |         |          |                      |     |              |
i
yˆ = (cid:14) (cid:14) ∈(0,1). (32) u n la b e l e d d a t as et w a s c re at e d u s i n g G N S 3 ( G l o b a l N e t w o r k
|     | i,k |     |     | ,k(cid:12)=y˜ | ,   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
K− i S im u l a t o r 3 ) , a w i d el y u s e d t o o l f o r s im u l a ti n g n e t w o r k
1
environments.Inthissetup,weconfiguredasimulatedCisco
(cid:11)K
CE(p ,y˜ )=− yˆ logp [k], router with NetFlow, a service that collects and monitors
|     | i   | i   | i,k | i   |     |     |     |            |      |       |        |         |             |            |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | ----- | ------ | ------- | ----------- | ---------- |
|     |     |     |     |     |     |     |     | IP traffic | data | as it | passes | through | the router. | The router |
k=1
(cid:11)K acted as a NetFlow exporter, sending traffic information
RCE(y˜ ,p )=− p [k] logyˆ . (33) to a virtual server set up as a NetFlow collector. This
|     | i   | i   |     | i   | i,k |     |     |                 |     |           |        |     |        |              |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --------- | ------ | --- | ------ | ------------ |
|     |     |     |     |     |     |     |     | virtual server, |     | operating | within | a   | VMware | environment, |
k=1
| 9110 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME6,2025 |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ |

TABLE2. Numberofflowsperclassintheself-generateddatasetandtheISCX
VPN-nonVPNdataset,withclassshareoverthecombinedcorpus.
FIGURE4. Diagramofthenetworkarchitectureandflowchartoftheunlabeled
datasetgenerationusingNetFlow.
processed NetFlow packets sent from the router, extracting
features from the traffic generated by a Windows 10 virtual
machine workstation running 10 distinct applications. These
applications were carefully selected to represent different
types of network traffic: VPN traffic (e.g., VPN_Vimeo,
Tor_YouTube), time-sensitive traffic (e.g., Skype_VideoCall, testing traffic classification models in realistic scenarios,
Facebook_Audio), file transfer traffic (e.g., FTPS_Upload, especially where encryption and varying network states
SFTP_Upload, SCP_Download), and video/voice traffic are involved. To adapt this dataset for our needs, we
(e.g., YouTube, Skype_Chat, Email). This variety ensures used custom Python scripts to process the.pcap files and
the dataset covers a broad range of network behaviors seen extractflow-leveltrafficdata.Thisinvolvedanalyzingpacket
in real-world scenarios. The combined network architecture sequences, grouping them into flows based on attributes
and dataset-generation workflow are shown in Fig. 4. like source/destination IP addresses and port numbers, and
The captured NetFlow data were then processed using selectingasubsetof538flows,chosentolimitlabelingeffort
a custom Python script that follows this workflow on the and ensure only complete flows were included. These flows
NetFlow collector, handling both feature extraction and matchthesame10applicationcategoriesasthelargedataset,
feature generation. The script extracted statistical features, ensuringconsistency.Thissmallerdatasetservesasalabeled
like packet count, octet count, and throughput, along with resource for fine-tuning the model, despite its much smaller
time-based attributes such as duration and inter-arrival size compared to the self-generated dataset. To reflect real-
times. In the “generation” step, the script also processed world traffic distributions, the number of flows per class
raw NetFlow packets to calculate additional features (e.g., was intentionally varied, resulting in an imbalanced dataset.
minimum, maximum, mean, and standard deviation of some This distribution is detailed in Table 2, which enumerates
features). The final dataset, saved as a Comma-Separated the flow counts for each class.
Values(CSV)file,contains21featuresand8,684flows.The UCDavis-QUICDataset:Weadditionallyevaluateonthe
combined corpus is intentionally imbalanced, reflecting real UCDavis-QUIC dataset, which contains QUIC-only traffic
traffic mixes: YouTube accounts for 41.9% of flows, while from five Google services (Google Docs, Google Drive,
minority classes such as SFTP_Upload and SCP_Download Google Music, Google Search, and YouTube). The released
are each under 4.5%. This skew is typical in NTC and data are packet captures (PCAP) from which flows are
is handled in our pipeline by class-aware thresholds and derived; in our pipeline, we convert PCAP to CSV and
balanced retention in the CL stage. Feature distributions are aggregate by 5-tuple to obtain per-flow statistics. Consistent
physically plausible and heavy-tailed, as expected for flows: withtheoriginalpaperofthedataset[40],weemployaflow-
themedian MeanPacket Length is571B(95thpercentile= level feature schema of 24 numerical statistics per flow. In
1,406 B, below the Ethernet MTU), the median Mean IAT addition,weretainanexplicitcategoricalflow-directionindi-
is 6.9 ms (95th percentile = 0.59 s). cator(forward/backward/bidirectional)alongsidethenumeric
ISCX VPN-nonVPN as a Small Labeled Dataset: The features. The QUIC dataset contains 6,439 flows in total. To
smaller labeled dataset was derived from the ISCX VPN- mirrorourlabel-scarcesetting,wetreatonly5%offlowsper
nonVPNdataset[12],awell-knownpublicdatasetdeveloped class as labeled and the remaining 95% as unlabeled, like
for NTC research. This dataset is originally provided in previous datasets. Table 3 reports the class distribution and
packet-level as.pcap files, which contain detailed captures the stratified labeled/unlabeled split, making the dataset’s
of network packets from various activities. It includes a imbalance explicit.
mix of VPN and non-VPN traffic, covering both encrypted We conducted our experiments on a workstation run-
and unencrypted flows across different applications and ning Ubuntu 22.04.4 LTS, Python 3.12.11, and PyTorch
conditions. This diversity makes it a strong benchmark for 2.8.0+cu126, equipped with an Intel Xeon CPU @
VOLUME6,2025 9111

ESLAMIANDHAMOUDA:NTCUSINGSSLANDCL
TABLE4. RepresentativegridsearchresultsforAE’shyperparameters.
TABLE5. RepresentativegridsearchresultsforTabCL’shyperparameters.
TABLE6. Representativegridsearchresultsforhyperparametersofconfidentlearningandfinalclassifier.
TABLE3.
UCDavis–QUICclassdistribution. ISCXVPN-nonVPNdatasetwasusedtofine-tunethemodel.
Thiscombinationeffectivelyaddressesthescarcityoflabeled
|     |     |     |     |     |     |     | data while | leveraging | the | strengths of | both datasets. |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | --- | ------------ | -------------- | --- |
Themodel’sperformanceismeasuredusingthefollowing
|     |     |     |     |     |     |     | metrics. In | these           | metrics, | TP, TN, FP, | and FN denote | true       |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --------------- | -------- | ----------- | ------------- | ---------- |
|     |     |     |     |     |     |     | positives,  | true negatives, | false    | positives,  | and false     | negatives, |
respectively.
|     |     |     |     |     |     |     | • Accuracy: | The         | proportion | of correctly | classified | sam-   |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----------- | ---------- | ------------ | ---------- | ------ |
|     |     |     |     |     |     |     | ples.       | This metric | provides   | an overall   | measure    | of the |
|     |     |     |     |     |     |     | model’s     | correctness | across     | all classes, | defined    | as:    |
TP+TN
2.00 GHz, 12.7 GB RAM, and a single NVIDIA Tesla T4 Accuracy= . (35)
TP+TN+FP+FN
| (15.0 GB) | GPU. |     |     |     |     |     |           |        |           |                      |            |            |
| --------- | ---- | --- | --- | --- | --- | --- | --------- | ------ | --------- | -------------------- | ---------- | ---------- |
|           |      |     |     |     |     |     | • Recall: | The    | ratio of  | correctly identified | positive   | sam-       |
|           |      |     |     |     |     |     | ples.     | Recall | indicates | the model’s          | ability to | detect all |
B. PERFORMANCEOFTHEPROPOSEDMODELON relevant instances of a class, given by:
SELF-GENERATEDANDISCXDATASETS
TP
This subsection evaluates theproposed model’s performance Recall= . (36)
TP+FN
| on Self-generated |     | and | ISCX | datasets, | focusing | on the |     |     |     |     |     |     |
| ----------------- | --- | --- | ---- | --------- | -------- | ------ | --- | --- | --- | --- | --- | --- |
• Precision:Theproportionofcorrectlypredictedpositive
| accuracy | of pseudo-label |     | generation |     | via SSL and | the final |     |     |     |     |     |     |
| -------- | --------------- | --- | ---------- | --- | ----------- | --------- | --- | --- | --- | --- | --- | --- |
classificationaccuracyachievedafterapplyingCLtomitigate samples among all samples predicted as positive,
|                                                        |     |     |        |           |            |           | calculated | as: |            |     |     |      |
| ------------------------------------------------------ | --- | --- | ------ | --------- | ---------- | --------- | ---------- | --- | ---------- | --- | --- | ---- |
| noisy pseudo-labels.                                   |     |     | During | training, | we treated | the self- |            |     |            |     |     |      |
| generateddatasetasunlabeled,usingitsassignedlabelsonly |     |     |        |           |            |           |            |     |            | TP  |     |      |
|                                                        |     |     |        |           |            |           |            |     | Precision= |     | .   | (37) |
TP+FP
| for evaluation | purposes. |     | By  | keeping | the dataset | unlabeled |     |     |     |     |     |     |
| -------------- | --------- | --- | --- | ------- | ----------- | --------- | --- | --- | --- | --- | --- | --- |
during training, we relied on SSL to uncover patterns from • F1-Score: The harmonic mean of precision and recall.
the plentiful unlabeled data. Meanwhile, the small labeled The F1-score balances precision and recall, offering a
| 9112 |     |     |     |     |     |     |     |     |     |     | VOLUME6,2025 |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- |

TABLE7. Hyperparametersofmodels(finalchoicesusedinevaluation).
singlemetricthatreflectstheperformanceofthemodel,
computed as:
Precision×Recall
F1-Score=2× . (38)
Precision+Recall
The above metrics collectively offer a robust assessment of
the model’s classification capabilities.
Regarding the hyperparameter selection, we tuned each
module with a stratified 5-fold cross-validation (CV) on the
small labeled ISCX split; for every candidate configuration,
we repeated training with 3 random seeds and reported
Macro-F1 as mean ± 95% CI over the resulting 15 scores
(5 folds × 3 seeds). We then selected the best settings
per module by Macro-F1 and carried those forward to the
end-to-end pipeline. Tables 4–6 present representative con-
figurations from the full grid used to select hyperparameters
for AE, TabCL, CL, and the final classifier. Finally, Table 7
presentsthearchitectureandhyperparametersforthemodels
utilized in the evaluation section.
1) SELF-SUPERVISEDLEARNINGFORPSEUDO-LABEL
GENERATION
Two SSL techniques were employed to assign pseudo-
labels to the unlabeled dataset: AE and TabCL. These
methods were applied separately as pretraining strategies on
TABLE8. PerformancemetricsforSSLpseudo-labeling.
the unlabeled corpus (8684 flows), followed by fine-tuning
with the small labeled set. The pseudo-label accuracy is
87.17% for AE and 89.22% for TabCL. We also evaluated
a confidence–margin voting fusion that consolidates AE
and TabCL predictions by agreement, which yields 89.91%
accuracy—an incremental gain over TabCL alone. In fusion,
the improvement is modest because TabCL already provides
TABLE9. Per-classperformanceofthefinalclassifier.
strong representations and the two models’ errors partially
overlap; however, fusion slightly increases precision, which
is beneficial for the downstream confident-learning filter.
Confusion matrices are presented in Fig. 5, illustrating the
alignment between pseudo-labels and true labels. Detailed
metrics appear in Table 8.
2) FINALCLASSIFIERWITHCONFIDENTLEARNING
For training the final classifier, we use the fused pseudo-
labels produced by the confidence–margin voting of AE
and TabCL from the previous subsection (Fig. 5, Table 8).
The fused pool attains an overall pseudo-label accuracy of
89.91%, implying that roughly 10% of labels are noisy. If
thisnoiseisnotaddressedandthefinalmultilayerperceptron
(MLP)istraineddirectlyonthefusedpseudo-labels,thetest
accuracyplateausat90.9%.Toimproverobustness,weapply
traffic-adapted CL to estimate per-sample label reliability
and downweight likelyerrorsbeforefinaltraining.WithCL, of the final classifier across individual classes, indicating
thefinalMLPreachesanaccuracyof96.29%.Theconfusion thatclass-imbalanceeffectswereeffectivelymitigatedbythe
matrix for the final classifier is shown in Fig. 6, and per- traffic-adapted CL stage.
classmetricsarereportedinTable 9,whichshowsuniformly Table 10 summarizes a comprehensive ablation across
high scores across most classes, with the few lower metrics three axes. (i) Pseudo-label source: keeping the down-
because of feature similarity between these types of traffic. stream CL+MLP stage fixed, we vary the source of
Additionally, a bar chart in Fig. 7 illustrates the accuracy pseudo-labels (AE, TabCL, or their fusion). Fusion delivers
VOLUME6,2025 9113

ESLAMIANDHAMOUDA:NTCUSINGSSLANDCL
FIGURE5. ConfusionmatricesofSSLmodelsforaddingpseudo-labels:(a)Autoencoder,(b)TabCL.
FIGURE7. Per-classaccuracyoffinalclassifier.
reach the best accuracy and macro-F1 with a small labeled
FIGURE6. ConfusionmatrixfortheMLPfinalclassifieronthetestdataset.
dataset.
Here, we report the computational footprint of the two
SSL pre-training strategies, the CL method, and the final
training. All values are the mean over 10 runs with
consistent gains over either branch alone, indicating that different random seeds. As summarized in Table 11, the
higher-quality, lower-noise pseudo-labels translate directly AE is lightweight with 31.19 s per full training round
into stronger downstream performance. (ii) CL variants: and 1.2 GB peak VRAM, while TabCL trades additional
reporting CL ablations separately for AE, TabCL, and compute for higher-quality representations: 107.86 s per
Fusion pseudo-labels, we progressively enrich CL from a round(≈3.5×AE)and1.5GBpeakVRAM.Thegapmainly
basic mean-threshold filter to our traffic-adapted pipeline comes from contrastive objectives (multi-view generation
(quantile thresholds, logistic weighting, and BRC). Each and similarity computations). The CL & final MLP stage is
additionyieldsmeasurableimprovements,demonstratingthat the smallest (24.85 s/round, 0.90 GB; 0.018 M parameters)
the traffic-aware CL design outperforms the original CL andprocessesflowsfastest(31,240flows/s),andthepseudo-
heuristic.(iii)Componentcontribution:isolatingcomponents labelingpassitselfisnotthebottleneck(AE:93,464flows/s;
shows that either SSL (without CL) or CL (without SSL TabCL:88,409flows/s),confirmingthatSSLpretraining,not
pretraining,justpseudo-labelingwithasmalllabeleddataset) CL/final training, dominates cost. All stages fit comfortably
is insufficient; the full pipeline (SSL + CL) is required to on a 15 GB T4 and keep peak memory below 2 GB,
9114 VOLUME6,2025

TABLE10. Ablationofthefinalstage.
FIGURE8. Per-classdistributionsoftheself-confidencesiforallpseudo-labeled
flows.
t0.7.
| magenta | solid line | is  | the quantile | threshold |     | Clean |
| ------- | ---------- | --- | ------------ | --------- | --- | ----- |
j
| classes | in the SSL | output | (e.g., | YouTube, | FTPS_Upload, |     |
| ------- | ---------- | ------ | ------ | -------- | ------------ | --- |
≈
| and Email) | exhibit   | sharply | peaked      | histograms |                     | near s i |
| ---------- | --------- | ------- | ----------- | ---------- | ------------------- | -------- |
| 0.9–1.0,   | small MAD | (≈      | 0.03–0.05), |            | and correspondingly |          |
TABLE11. high thresholds t0.7 ∈ [0.90,0.92]. In contrast, classes that
ComputeprofileofSSLandCL/finaltraining. j
| were noisier | in the | SSL | (e.g., | Skype_Chat, | SFTP_Upload, |     |
| ------------ | ------ | --- | ------ | ----------- | ------------ | --- |
andFacebook_Audio)showbroader,left-shifteddistributions
|             |      | (≈     | 0.07–0.11) |            |            |          |
| ----------- | ---- | ------ | ---------- | ---------- | ---------- | -------- |
| with larger | MAD  |        |            | and        | noticeably | lower    |
|             |      | t0.7   |            | 0.74–0.82. |            |          |
| thresholds, | with | moving |            | to         | This       | leftward |
j
| adjustment    | is intentional: |         | it          | prevents    | aggressive | pruning   |
| ------------- | --------------- | ------- | ----------- | ----------- | ---------- | --------- |
| of inherently | harder          | classes | by          | requiring   | a less     | stringent |
| confidence    | to contribute   |         | significant | weight.     | The dashed | gray      |
| mean lines    | are             | often   | left of     | the magenta | t0.7       | in clean  |
j
| classes due | to right-skew; |        | using      | the quantile | rather     | than the |
| ----------- | -------------- | ------ | ---------- | ------------ | ---------- | -------- |
| mean avoids | being          | unduly | influenced |              | by a small | tail of  |
indicating they are deployable on commodity GPUs. In low-confidence samples. Conversely, in noisy classes, the
terms of scalability, throughput scales near-linearly with quantile naturally tracks lower, reflecting the heavier mass
the number of flows, supporting larger datasets. This low at moderate confidences. These adaptive thresholds feed our
overhead enables deployment in real-world scenarios, such CL weighting. As a result, the final classifier trained with
as edge networks for online traffic analysis. SSL pretraining CL improves from 90.9% (no CL) to 96.29% accuracy.
canbeparallelizedacrossworkersorscheduledoffline,while The largest per-class gains occur exactly where Fig. 8
t0.7
the CL & final MLP update remains quick and memory- indicates higher noise and lower (e.g., Skype_Chat,
j
frugal for frequent refreshes. Overall, the compute profile SFTP_Upload, and Facebook_Audio), confirming that the
demonstrates efficiency (minutes per round) and resource performance gap between SSL pseudo-labeling and the final
frugality for scalable NTC applications. model is attributable to the CL stage.
Fig. 8 visualizes how CL adapts its per-class decision To further validate our approach, we compare our frame-
thresholds to the reliability of the pseudo-labels. The work with five recent approaches that span supervised deep
dashed gray line is the class mean (original CL), and the modelsandSSLparadigms:anMTEFUmodelthatcombines
VOLUME6,2025 9115

ESLAMIANDHAMOUDA:NTCUSINGSSLANDCL
TABLE12. Performancemetricsofourmodelandstate-of-the-artmethods.
TABLE13.
CNN/SAE/GRU/LSTM heads under a shared architecture UCDavis–QUIC:SSLpseudo-labelingmetrics.
| (supervised) | [34],           | TFE-GNN |        | (supervised,    |         | graph       | neural    |     |     |     |     |     |     |     |     |
| ------------ | --------------- | ------- | ------ | --------------- | ------- | ----------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| model)       | [33], FlowPic   |         | with   | self-supervised |         | contrastive | pre-      |     |     |     |     |     |     |     |     |
| training     | on mini-FlowPic |         | images | [18],           | ET-BERT |             | [19] with |     |     |     |     |     |     |     |     |
transformerunsupervisedpretrainingfollowedbysupervised
fine-tuningonlimitedlabelsatpacket/flowlevel,andanSSL
| approach | for encrypted |               | traffic[21].      |     | To make   | the          | comparison |          |         |       |              |            |     |             |     |
| -------- | ------------- | ------------- | ----------------- | --- | --------- | ------------ | ---------- | -------- | ------- | ----- | ------------ | ---------- | --- | ----------- | --- |
| fair and | reproducible, |               | we re-implemented |     |           | (or followed | the        |          |         |       |              |            |     |             |     |
|          |               |               |                   |     |           |              |            | selected | exactly | as in | the previous | subsection |     | (stratified | 5-  |
| authors’ | public        | descriptions) |                   | and | evaluated | all          | baselines  |          |         |       |              |            |     |             |     |
foldCVonthesmalllabeledsplit;threeseedspercandidate;
under our datasets. Specifically, methods that require labels select by Macro-F1). Given the lower number of classes
| only (TFE-GNN |     | and | multitask | fusion) |     | were | trained on |         |        |             |     |         |         |      |       |
| ------------- | --- | --- | --------- | ------- | --- | ---- | ---------- | ------- | ------ | ----------- | --- | ------- | ------- | ---- | ----- |
|               |     |     |           |         |     |      |            | (5) and | a more | homogeneous |     | feature | schema, | only | minor |
the self-generated dataset and evaluated on the same test changes were adopted: based on grid search, for the AE we
| partitions | as ours;      | methods | that     | require | unlabeled |             | + a small |                |         |              |        |           |              |              |      |
| ---------- | ------------- | ------- | -------- | ------- | --------- | ----------- | --------- | -------------- | ------- | ------------ | ------ | --------- | ------------ | ------------ | ---- |
|            |               |         |          |         |           |             |           | use a slightly | smaller |              | latent | size (64) | to curb      | overfitting; | in   |
| labeled    | set (FlowPic, |         | ET-BERT, | Towhid  |           | & Shahriar) | were      |                |         |              |        |           |              |              |      |
|            |               |         |          |         |           |             |           | TabCL we       | reduce  | augmentation |        | intensity | (replacement |              | rate |
provided our self-generated corpus as unlabeled plus the r = 0.10) and temperature (τ = 0.4, τ = 0.15) to
|            |         |        |           |     |       |          |        |             |          |             |     | cont       |     | cat   |           |
| ---------- | ------- | ------ | --------- | --- | ----- | -------- | ------ | ----------- | -------- | ----------- | --- | ---------- | --- | ----- | --------- |
| same small | labeled | split, | mirroring |     | their | intended | usage. |             |          |             |     |            |     |       |           |
|            |         |        |           |     |       |          |        | reflect the | smoother | intra-class |     | structure; | in  | CL we | raise the |
As summarized in Table 12, our framework achieves quantile threshold to q = 0.75 and use a steeper logistic
| 96.29%accuracywhileusingonlyasmalllabeledseed,out- |         |          |     |             |     |               |     | γ     | =6  |         |           |      |          |        |     |
| -------------------------------------------------- | ------- | -------- | --- | ----------- | --- | ------------- | --- | ----- | --- | ------- | --------- | ---- | -------- | ------ | --- |
|                                                    |         |          |     |             |     |               |     | slope | to  | be more | selective | with | residual | noise. |     |
| performing                                         | FlowPic | (93.73%) |     | and ET-BERT |     | (91.64%)under |     |       |     |         |           |      |          |        |     |
our setting, and exceeding the supervised TFE-GNN and 1) SELF-SUPERVISEDLEARNINGFORPSEUDO-LABEL
multitask-fusion baselines despite their access to labeled GENERATION(QUIC)
training data. Despite those powerful pre-training strategies, WeapplybothSSLbranchesindependentlyontheunlabeled
+
our SSL CL pipeline delivers higher accuracy with QUIC flows and then fine-tune on the 5% labeled split.
| far fewer | labels, | indicating |     | that flow-tabular |     | representation |     |              |             |     |     |          |         |            |     |
| --------- | ------- | ---------- | --- | ----------------- | --- | -------------- | --- | ------------ | ----------- | --- | --- | -------- | ------- | ---------- | --- |
|           |         |            |     |                   |     |                |     | Pseudo-label | performance |     | on  | the full | dataset | is strong: | the |
learning combined with noise-aware CL is competitive AE reaches 94.07% accuracy, TabCL improves to 95.65%,
with image- and transformer-based pre-training while being and a confidence–margin voting fusion gives a further lift to
| label-efficient. |     | Beyond | the | headline | accuracy, |     | our frame- |     |     |     |     |     |     |     |     |
| ---------------- | --- | ------ | --- | -------- | --------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
96.11%.Class-wiseconfusionpatternsforAEandTabCLare
work operates end-to-end—from raw packet capture to shown in Fig. 9. Aggregate metrics of SSL pseudo-labeling
| flow aggregation, |     | pseudo-labeling, |     |     | noise | filtering, | and final |              |          |     |     |     |     |     |     |
| ----------------- | --- | ---------------- | --- | --- | ----- | ---------- | --------- | ------------ | -------- | --- | --- | --- | --- | --- | --- |
|                   |     |                  |     |     |       |            |           | are detailed | in Table | 13. |     |     |     |     |     |
classification—so it can be deployed in realistic “low-label” For completeness, we profiled the SSL round times
settings rather than only curated benchmarks. Evaluations on the same workstation used earlier. Owing to the
| on our | controlled, | end-to-end |     | corpus | and | on  | the public |         |        |        |       |           |              |     |      |
| ------ | ----------- | ---------- | --- | ------ | --- | --- | ---------- | ------- | ------ | ------ | ----- | --------- | ------------ | --- | ---- |
|        |             |            |     |        |     |     |            | smaller | corpus | (6,439 | flows | vs. 8,684 | previously), |     | both |
ISCX subset indicate that the method scales to thousands branches are faster: AE averages 22.21s/round and TabCL
of flows and transfers with minimal tuning, suggesting 51.95s/round. Peak GPU memory is modest for both
good generalization while directly addressing label scarcity branches—about1.0GBforAEand1.3GBforTabCL.This
through SSL and CL. is consistent with the roughly linear scaling of through-
|                                    |     |     |     |     |     |     |     | put with    | the number |     | of flows | observed |     | in the | previous |
| ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | --- | -------- | -------- | --- | ------ | -------- |
| C. PERFORMANCEOFTHEPROPOSEDMODELON |     |     |     |     |     |     |     | subsection. |            |     |          |          |     |        |          |
UCDAVIS–QUIC
Tostress-testgeneralizationbeyondourself-generated/ISCX 2) FINALCLASSIFIERWITHCONFIDENTLEARNING
(QUIC)
| setting, | we further | evaluate |     | on the | UCDavis–QUIC |     | dataset |     |     |     |     |     |     |     |     |
| -------- | ---------- | -------- | --- | ------ | ------------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
with five Google services (Docs, Drive, Music, Search, We then pass the fused pseudo-labeled pool into traffic-
YouTube).Inkeepingwithour“low-label”protocol,wetreat adapted CL and train the final MLP. The resulting model
5% of flows per class as the small labeled set and the attains 98.76% ± 0.10 accuracy. The confusion matrix
remaining95%asunlabeled(Table 3).Hyperparametersare is shown in Fig. 10. Per-class precision, recall, F1, and
| 9116 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME6,2025 |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- |

FIGURE9. UCDavis–QUIC:confusionmatricesofSSLpseudo-labelers.
TABLE14. UCDavis–QUIC:per-classperformanceofthefinalclassifier. TABLE15. AblationonUCDavis–QUIC.
per-class accuracy are reported in Table 14. Scores are
uniformly high; the few residual errors arise primarily from
semanticallysimilarservices(e.g.,Musicvs.YouTube,Docs
vs. Search).
Table 15 consolidates three ablations using the same
protocol as before (mean over 10 seeds). (i) Pseudo-
label source. Holding the downstream CL+MLP fixed, (ii)
CL variants based on AE, TabCL, and Fusion pseudo-
labels.Startingfrom“No-CL”,progressivelyaddingquantile
thresholds, logistic weighting, and our BRC step yields
monotonic gains, evidence that the traffic-adapted CL is
more effective than the original mean-threshold heuristic.
(iii) Component contribution Neither SSL (without CL) nor
CL (without SSL pretraining) is sufficient; the full SSL+CL
pipeline is required to reach the best accuracy/F1 with only
5% labels.
Finally, Table 16 contrasts our method with three repre-
sentative baselines that report results on UCDavis–QUIC.
FlowPic’s QUIC “script” setting reports 98.3% accuracy;
the multitask fusion model reports ≈ 94.7% for “Class”
prediction; the SSL method of Towhid & Shahriar reports
≈ 98% depending on the pretraining ratio. As seen, our acrossthreedatasets(intwoevaluationsettings)andremains
SSL+ CLpipelineattainsthestrongestoverallscoresonthis competitive even against specialized supervised or SSL
dataset as well, reinforcing that the framework generalizes baselines.
VOLUME6,2025 9117

ESLAMIANDHAMOUDA:NTCUSINGSSLANDCL
TABLE16. UCDavis–QUIC:comparisonourmodelwithstate-of-the-artmethods.
pseudo-labeling,noisemitigation,andclassification,support-
|     |     |     |     |     |     |     |     | ing realistic  | “low-label”      |                 | deployments.    |                    | Nevertheless,      |               | some       |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ---------------- | --------------- | --------------- | ------------------ | ------------------ | ------------- | ---------- |
|     |     |     |     |     |     |     |     | limitations    | remain.          | The             | current         | framework          |                    | relies        | on offline |
|     |     |     |     |     |     |     |     | pretraining,   | which            | may             | limit           | its                | applicability      |               | in high-   |
|     |     |     |     |     |     |     |     | throughput     | real-time        |                 | systems         | or when            | traffic            | distributions |            |
|     |     |     |     |     |     |     |     | drift quickly. |                  | While           | we evaluated    |                    | the framework      |               | on three   |
|     |     |     |     |     |     |     |     | datasets       | in two           | settings,       | its performance |                    | could              | be influenced |            |
|     |     |     |     |     |     |     |     | by dataset     | diversity;       |                 | for instance,   | rare               | enterprise         |               | apps and   |
|     |     |     |     |     |     |     |     | emerging       | protocols        | may             | be              | under-represented. |                    | Additionally, |            |
|     |     |     |     |     |     |     |     | scaling        | the pipeline     |                 | to real-time,   | high-volume        |                    | traffic       | with       |
|     |     |     |     |     |     |     |     | tight latency  | requirements     |                 |                 | remains            | challenging.       | Moreover,     |            |
|     |     |     |     |     |     |     |     | network        | traffic          | data            | are inherently  |                    | privacy-sensitive; |               | com-       |
|     |     |     |     |     |     |     |     | pliance        | and data-sharing |                 | constraints     |                    | can limit          | training      | and        |
|     |     |     |     |     |     |     |     | cross-site     | evaluation.      |                 | To              | address            | these,             | future        | research   |
|     |     |     |     |     |     |     |     | could extend   |                  | the approach    |                 | to online          | incremental        |               | learning   |
|     |     |     |     |     |     |     |     | that refreshes |                  | representations |                 | and class-wise     |                    | thresholds    | for        |
dynamicenvironments,incorporatebroaderandmorediverse
datasetstoenhancegeneralization,developscalablereal-time
| FIGURE10. | UCDavis–QUIC:confusionmatrixofthefinalMLPwithCL. |     |     |     |     |     |     |           |           |                          |     |     |     |           |     |
| --------- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --------- | --------- | ------------------------ | --- | --- | --- | --------- | --- |
|           |                                                  |     |     |     |     |     |     | variants, | integrate | open-world/unknown-class |     |     |     | handling, | and |
federatedtrainingforprivacy-preservingmulti-sitescenarios.
VI. CONCLUSION
| This paper | presented | an  | end-to-end | framework |     | for NTC | that |     |     |     |     |     |     |     |     |
| ---------- | --------- | --- | ---------- | --------- | --- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
REFERENCES
| couples | SSL with | a traffic-adapted |     |     | CL stage | and | a final |     |     |     |     |     |     |     |     |
| ------- | -------- | ----------------- | --- | --- | -------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
weightedMLPclassifier.TwocomplementarySSLbranches, [1] A. Azab, M. Khasawneh, S. Alrabaee, K. K. R. Choo, and
M.Sarsour,“Networktrafficclassification:Techniques,datasets,and
anAEwithconstraint-consistentreconstructionandaTabCL challenges,” Digit. Commun. Netw., vol.10, no.3, pp.676–692,
| with class-conditioned |              |               | views | and dual-head |           | temperatures, |        | Jun.2024. |             |             |     |         |          |           |            |
| ---------------------- | ------------ | ------------- | ----- | ------------- | --------- | ------------- | ------ | --------- | ----------- | ----------- | --- | ------- | -------- | --------- | ---------- |
|                        |              |               |       |               |           |               |        | [2] M.    | Saqib,      | H. Elbiaze, | and | R. H.   | Glitho,  | “Adaptive | in-network |
| produce                | high-quality | pseudo-labels |       | from          | unlabeled |               | flows. | A         |             |             |     |         |          |           |            |
|                        |              |               |       |               |           |               |        | traffic   | classifier: | Bridging    | the | gap for | improved | QoS by    | minimizing |
confidence–margin voting fusion consolidates the branches, misclassification,”IEEEOpenJ.Commun.Soc.,vol.5,pp.677–689,
| and the       | downstream |          | CL module   | denoises          |       | pseudo-labels |          | 2024.       |       |           |           |              |          |           |            |
| ------------- | ---------- | -------- | ----------- | ----------------- | ----- | ------------- | -------- | ----------- | ----- | --------- | --------- | ------------ | -------- | --------- | ---------- |
|               |            |          |             |                   |       |               |          | [3] (Cisco, | San   | Jose, CA, | USA).     | Cisco Annual | Internet | Report    | (2018–     |
| via per-class | quantile   |          | thresholds, | calibration-aware |       |               | logistic |             |       |           |           |              |          |           |            |
|               |            |          |             |                   |       |               |          | 2023)       | White | Paper.    | Accessed: | Mar.         | 9, 2020. | [Online]. | Available: |
| weighting,    | and        | balanced | retention   | before            | final | training      | with     |             |       |           |           |              |          |           |            |
https://www.cisco.com/c/en/us/solutions/collateral/executive-
| symmetric | cross-entropy. |     | Across | three | datasets | and | two |     |     |     |     |     |     |     |     |
| --------- | -------------- | --- | ------ | ----- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
perspectives/annual-internet-report/white-paper-c11-741490.html.
|           |               |     |             |     |                      |     |     | [4] Y. Feng | et  | al., “Unmasking |     | the Internet: | A survey | of  | fine-grained |
| --------- | ------------- | --- | ----------- | --- | -------------------- | --- | --- | ----------- | --- | --------------- | --- | ------------- | -------- | --- | ------------ |
| settings, | the framework |     | is accurate |     | and label-efficient. |     | On  |             |     |                 |     |               |          |     |              |
networktrafficanalysis,”IEEECommun.SurveysTuts.,earlyaccess,
| our deployment-style |     | pipeline |     | built from | raw | packet | capture |     |     |     |     |     |     |     |     |
| -------------------- | --- | -------- | --- | ---------- | --- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
Feb.25,2025,doi:10.1109/COMST.2025.3545541.
(self-generated unlabeled corpus) and a small ISCX VPN– [5] E.Paolini,L.Valcarenghi,L.Maggiani,andN.Andriolli,“Real-time
nonVPN labeled split, the final model attains 96.29% network packet classification exploiting computer vision architec-
tures,”IEEEOpenJ.Commun.Soc.,vol.5pp.1155–1166,2024.
| accuracy | with strong |     | macro-F1, | while | remaining | resource- |     |        |           |            |     |             |     |       |            |
| -------- | ----------- | --- | --------- | ----- | --------- | --------- | --- | ------ | --------- | ---------- | --- | ----------- | --- | ----- | ---------- |
|          |             |     |           |       |           |           |     | [6] A. | Shahraki, | M. Abbasi, | A.  | Taherkordi, | and | A. D. | Jurcut, “A |
frugal. On the public UCDavis–QUIC dataset, using only comprehensive survey on 6G networks: Applications, core services,
5% of flows per class as labeled, the method reaches enablingtechnologies,andchallenges,”Jan.2021,arXiv:2101.12475.
|     |     |     |     |     |     |     |     | [7] M. | Abbasi, | A. Shahraki, | and | A. Taherkordi, |     | “Deep | learning for |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------- | ------------ | --- | -------------- | --- | ----- | ------------ |
98.76% accuracy and uniformly high per-class scores, networktrafficmonitoringandanalysis(NTMA):Asurvey,”Comput.
outperforming strong supervised and SSL baselines reported Commun.,vol.170,pp.19–33,Mar. 2021.
on the same data. Ablations confirm that (i) higher-quality [8] D. Di Monda, A. Montieri, V. Persico, P. Voria, M. De Ieso,
|               |           |     |                            |     |     |     |       | and       | A. Pescapè, | “Few-shot |     | class-incremental |            | learning | for network |
| ------------- | --------- | --- | -------------------------- | --- | --- | --- | ----- | --------- | ----------- | --------- | --- | ----------------- | ---------- | -------- | ----------- |
| pseudo-labels | (AE/TabCL |     | fusion)translateintobetter |     |     |     | down- |           |             |           |     |                   |            |          |             |
|               |           |     |                            |     |     |     |       | intrusion | detection   | systems,” |     | IEEE Open         | J. Commun. |          | Soc., vol.5 |
stream performance, and (ii) the traffic-adapted CL design pp.6736–6757,2024.
|            |          |      |         |                |     |            |     | [9] P. Khandait, |     | N. Hubballi, | and | B. Mazumdar, |     | “Efficient | keyword |
| ---------- | -------- | ---- | ------- | -------------- | --- | ---------- | --- | ---------------- | --- | ------------ | --- | ------------ | --- | ---------- | ------- |
| materially | improves | over | a basic | mean-threshold |     | heuristic. |     |                  |     |              |     |              |     |            |         |
matchingfordeeppacketinspectionbasednetworktrafficclassifica-
| Beyond   | headline | metrics, |     | the framework |     | provides |           | a      |          |      |            |         |       |                   |     |
| -------- | -------- | -------- | --- | ------------- | --- | -------- | --------- | ------ | -------- | ---- | ---------- | ------- | ----- | ----------------- | --- |
|          |          |          |     |               |     |          |           | tion,” | in Proc. | IEEE | Int. Conf. | Commun. | Syst. | Netw. (COMSNETS), |     |
| complete | solution | from     | raw | packets       | to  | flow     | features, |        |          |      |            |         |       |                   |     |
Mar.2020,pp.567–570.
| 9118 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME6,2025 |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- |

[10] A. Nascita, G. Aceto, D. Ciuonzo, A. Montieri, V. Persico, and [32] G. D’Angelo and F. Palmieri, “Network traffic classification using
A.Pescapé,“AsurveyonexplainableartificialintelligenceforInternet deepconvolutionalrecurrentautoencoderneuralnetworksforspatial–
traffic classification and prediction, and intrusion detection,” IEEE temporal features extraction,” J. Netw. Comput. Appl., vol.173,
Commun. Surveys Tuts., vol. 27, no. 5, pp.3165–3198, 4th Quart., Jan.2021,Art.no.102890.
2025. [33] H. Zhang et al., “TFE-GNN: A temporal fusion encoder using
[11] R.RaveendranandR.Menon,“AnefficientmethodforInternettraffic graph neural networks for fine-grained encrypted traffic classifica-
classificationandidentificationusingstatisticalfeatures,”Int.J.Eng. tion,”inProc.ACMWebConf.,Apr.2023,pp.2066–2075.
Res.Technol.,vol.4,no.7,pp.297–303,2015. [34] L. Liu, Y. Yu, Y. Wu, Z. Hui, and J. Hu, “Method for multi-task
[12] G. Draper-Gil, A. Habibi, M. Saiful, and A. Ghorbani, learningfusionnetworktrafficclassificationtoaddresssmallsample
“Characterization of encrypted and VPN traffic using time-related labels,” Sci.Rep.,vol.14,no.1,p.2518,Jan.2024.
features,” in Proc. 2nd Int. Conf. Inf. Syst. Secur. Privacy (ICISSP), [35] S. Dadkhah, H. Mahdikhani, P. K. Danso, A. Zohourian,
2016,pp.407–414. K.A.Truong, and A. A. Ghorbani, “Towards the development of a
[13] R.H.Serag,M.S.Abdalzaher,H.Elsayed,M.Sobh,M.Krichen,and realisticmultidimensionalIoTprofilingdataset,”inProc.19thAnnu.
M. Salim, “Machine-learning-based traffic classification in software- Int.Conf.Privacy,SecurityTrust(PST),Aug.2022,pp.1–11.
definednetworks,”Electronics, vol.13,no.6,p.1108,Mar. 2024. [36] W. Zhang, L. Zhang, X. Zhang, Y. Wang, P. Liu, and G. Gui,
[14] W. Lin and Y. Chen, “Robust network traffic classification based “Intelligent unsupervised network traffic classification method using
on information bottleneck neural network,” IEEE Access, vol.12, adversarial training and deep clustering for secure Internet of
pp.150169–150179,2024. Things,”FutureInternet, vol.15,no.9,pp.298–318,2023.
[15] Y. Ma, Z. Li, H. Xue, and J. Chang, “A balanced supervised [37] B.Gao,Y.Yang,Z.Gao,P.Yu,R.Lyu,andS.Chen,“Unsupervised
contrastive learning-based method for encrypted network traffic networktrafficclassificationbasedonmulti-sourcesynergisticdistri-
classification,”Comput.Secur.,vol.145,Oct.2024,Art.no.104023. butionalignment,”inProc.IEEEGlobalCommun.Conf.,Feb.2023,
pp.4313–4319.
[16] X. Xiao et al., “RBLJAN: Robust byte-label joint attention network
[38] M.A.Aleisa,“TrafficclassificationinSDN-basedIoTnetworkusing
for network traffic classification,” IEEE Trans. Dependable Secure
two-level fused network with self-adaptive manta ray foraging,” Sci.
Comput.,vol.22,no.3,pp.2161–2178,May/Jun.2025.
Rep.,vol.15,no.1,p.881,Jan.2025.
[17] K. Lin, X. Xu, and Y. Jiang, “A new semi-supervised approach
[39] S. Xu, J. Han, Y. Liu, H. Liu, and Y. Bai, “Few-shot traffic
for network encrypted traffic clustering and classification,” in Proc.
classification based on autoencoder and deep graph convolutional
IEEE Int. Conf. Comput. Support. Cooper. Work Design (CSCWD),
networks,”Sci.Rep.,vol.15,no.1,p.8995,Mar.2025.
May2022,pp.41–46.
[40] S. Rezaei and X. Liu, “How to achieve high classification accuracy
[18] E. Horowicz, T. Shapira, and Y. Shavitt, “Self-supervised traffic
with just a few labels: A semi-supervised approach using sampled
classification:Flowembeddingandfew-shotsolutions,”IEEETrans.
packets,” May2020,arXiv:1812.09761.
Netw.ServiceManag.,vol.21,no.3,pp.3054–3067,Jun.2024.
[19] X. Lin, G. Xiong, G. Gou, Z. Li, J. Shi, and J. Yu, “ET-
BERT: A contextualized datagram representation with pre-training
transformers for encrypted traffic classification,” in Proc. ACM Web
Conf.,Apr.2022,pp.633–642.
[20] R. Zhao et al., “Yet another traffic classifier: A masked autoencoder
basedtraffictransformerwithmulti-levelflowrepresentation,”inProc.
AAAIConf.Artif.Intell.,vol.37,2023,pp.5420–5427.
[21] M.TowhidandN.Shahriar,“Encryptednetworktrafficclassification
usingself-supervisedlearning,”inProc.IEEEInt.Conf.Netw.Softw.
(NetSoft),Aug.2022,pp.366–375.
[22] Y. Heng, V. Chandrasekhar, and J. G. Andrews,
“UTMobileNetTraffic2021: A labeled public network traffic
dataset,” IEEENetw.Lett., vol.3,no.3,pp.156–160,Sep.2021.
[23] J. L. Guerra, C. Catania, and E. Veas, “Datasets are not enough:
Challenges in labeling network traffic,” Comput. Secur., vol.120,
Jun.2022,Art.no.102810.
[24] D.Soukup,P.Tisovcˇík,K.Hynek,andT.Cˇejka,“Towardsevaluating
quality of datasets for network traffic domain,” in Proc. IEEE Int.
Conf.Netw.ServiceManag.(CNSM),2021,pp.264–268.
[25] J. Krupski, M. Iwanowski, and W. Graniszewski, “On the right
choice of data from popular datasets for Internet traffic classifica-
tion,”Comput.Commun.J.,vol.233,Mar.2025,Art.no.108068.
[26] C. G. Northcutt, L. Jiang, and I. L. Chuang, “Confident learning:
Estimatinguncertaintyindatasetlabels,”J.Artif.Intell.Res.,vol.70,
pp.1373–1411,Apr.2021.
[27] W. Cui, R. Hosseinzadeh, J. Ma, T. Wu, Y. Sui, and K. Golestan,
“Tabular data contrastive learning via class-conditioned and feature-
correlationbasedaugmentation,”Apr.2024,arXiv:2404.17489.
[28] N.Hubballi,M.Swarnkar,andM.Conti,“BitProb:Probabilistic Bit
SignaturesforAccurateApplicationIdentification,”IEEETrans.Netw.
ServiceManag.,vol.17,no.3,pp.1730–1741,Sep.2020.
[29] A.SalauandM.Beyene,“Softwaredefinednetworkingbasednetwork
traffic classification using machine learning techniques,” Sci. Rep., EHSAN ESLAMI (Student Member, IEEE)
vol.14,no.1,Aug.2024,Art.no.20060. receivedtheB.Sc.degreeincomputerengineering
from the University of Tabriz, Tabriz, Iran, in
[30] M. Lotfollahi, M. J. Siavoshani, R. S. H. Zade, and M. Saberian,
2022.HeiscurrentlypursuingtheM.Sc.degreein
“Deep packet: A novel approach for encrypted traffic classification
computerengineeringfromConcordiaUniversity,
using deep learning,” Soft Comput., vol.24, no.3, pp.1999–2012,
Montreal,QC,Canada.
2020.
His research interests include AI-powered
[31] A. Jenefa, S. Sam, V. Nair, B. G. Thomas, A. S. George, and
computer networks, federated learning, pro-
R.Thomas, “A robust deep learning-based approach for network
grammability of computer networks, and
trafficclassificationusingCNNsandRNNs,”inProc.IEEEInt.Conf.
software-definednetworking.
SignalProcess.Commun.(ICSPC),May2023,pp.106–110.
VOLUME6,2025 9119

ESLAMIANDHAMOUDA:NTCUSINGSSLANDCL
WALAA HAMOUDA (Senior Member, IEEE)
received the M.A.Sc. and Ph.D. degrees in elec-
trical and computer engineering from Queens
University, Kingston, ON, Canada, in 1998 and
2002, respectively. Since July 2002, he has been
with the Department of Electrical and Computer
Engineering,ConcordiaUniversity,Montreal,QC,
Canada, where he is currently a Professor. Since
June 2006, he is Concordia University Research
Chair Tier I in Wireless Communications and
Networking.Hiscurrentresearchinterestsinclude
machine-to-machinecommunications,IoT,5Gandbeyondtechnologies,sin-
gle/multiuser multiple-input–multiple-output communications, space-time
processing,cognitiveradios,andwirelessnetworks.Hereceivednumerous
awards, including the Best Paper Awards of the IEEE GC 2023, IEEE
GC 2020, IEEE ICC 2021, ICCSPA 2019, IEEE WCNC 2016, IEEE
ICC 2009, and the IEEE Canada Certificate of Appreciation in 2007
and 2008. He has been serving as the Co-Chair for the IoT and
Sensor Networks Symposium of the GC22, the TPC Co-Chair of the
ITC/ADC 2022 Conference, the Track Co-Chair for Antenna Systems,
Propagation, and RF Design, IEEE Vehicular Technology Conference
(VTC Fall’20), the Tutorial Chair for IEEE Canadian Conference in
Electrical and Computer Engineering (CCECE 2020), the General Co-
Chair, IEEE SmartNets 2019 Conference, the Co-Chair for the MAC
and Cross Layer Design Track of the IEEE (WCNC) 2019 and the
Wireless Communications Symposium of the IEEE ICC18 and the Ad-
hoc, Sensor, and Mesh Networking Symposium of the IEEE GC17, the
TechnicalCo-chairfortheFifthInternationalConferenceonSelectedTopics
in Mobile & Wireless Networking (MoWNet2016), the Track Co-Chair
for Multiple Antenna and Cooperative Communications, IEEE Vehicular
TechnologyConference(VTCFall’16),theCo-ChairforACMPerformance
EvaluationofWirelessAdHoc,Sensor,andUbiquitousNetworks(ACMPE-
WASUN’14) 2014, the Technical Co chair for the Wireless Networks
Symposium, the 2012 Global Communications Conference, the Ad hoc,
Sensor, and Mesh Networking Symposium of the 2010 ICC, and the 25th
Queens Biennial Symposium on Communications. He also served as the
Track Co-chair for the Radio Access Techniques of the 2006 IEEE VTC
Fall 2006 and the Transmission Techniques of the IEEE VTC-Fall 2012.
From September 2005 to November 2008, he was the Chair of the IEEE
Montreal Chapter in Communications and Information Theory. He is an
IEEEComSocDistinguishedLecturer.HeservedasanAssociateEditorfor
theIEEECOMMUNICATIONSLETTERS,IEEETRANSACTIONSONSIGNAL
PROCESSING, IEEECOMMUNICATIONSSURVEYSANDTUTORIALS, IET
Wireless Sensor Systems, IEEEWIRELESSCOMMUNICATIONSLETTERS,
TransactionsonVehicularTechnology,andcurrentlyservesasanEditorfor
the IEEETRANSACTIONSONCOMMUNICATIONS, IEEETRANSACTIONS
ON WIRELESS COMMUNICATIONS, and IEEE INTERNET OF THINGS
JOURNAL.
9120 VOLUME6,2025