Intelligent VPN Traffic Analysis and Classification
Framework on Raspberry Pi Using Machine
Learning Techniques
1st Mihai Bucurel 2nd Sebastian-Alexandru Dragusin 3rd Nicu Bizon
Faculty of Electronics, Communication Doctoral School of Electronics, Faculty of Electronics, Communication
and Computers Telecommunications & Information and Computers
National University of Science and Technology National University of Science and
Technology POLITEHNICA Bucharest, National University of Science and Technology POLITEHNICA Bucharest,
Pitești University Centre Technology POLITEHNICA Bucharest Pitești University Centre
Romania Romania Romania
bucurel@gmail.com sebastian.dragusin@upb.ro nicu.bizon1402@upb.ro
Abstract—The increasing adoption of Virtual Private signature-based detection mechanisms, which may be
Networks (VPNs) for secure communications has created new insufficient when dealing with large-scale and continuously
challenges regarding traffic monitoring, classification, and evolving network environments [7].
anomaly detection in resource-constrained environments. This
Recent advances in ML have demonstrated significant
paper presents an intelligent framework for VPN traffic
analysis and classification deployed on a Raspberry Pi platform. potential for improving network traffic analysis and
The proposed system combines secure VPN connectivity using cybersecurity monitoring [8]. Supervised learning algorithms
OpenVPN and WireGuard with real-time traffic monitoring such as RF and SVM have been successfully employed for
and machine learning (ML)-based analysis. Network traffic is traffic classification, anomaly detection, and intrusion
collected and processed using packet capture and inspection identification tasks [9], [10]. Furthermore, lightweight
tools, while Random Forest (RF) and Support Vector Machine artificial intelligence frameworks enable the deployment of
(SVM) models are employed to classify traffic flows and identify intelligent monitoring services directly on embedded and edge
potentially suspicious activities. Furthermore, TensorFlow Lite computing platforms, reducing latency and minimizing
is integrated to enable lightweight real-time inference on dependence on cloud-based infrastructures [2].
embedded hardware with limited computational resources.
Experimental evaluation demonstrates the feasibility of In parallel, edge computing has emerged as a promising
deploying intelligent traffic analysis services directly on edge paradigm for processing data closer to its source [11]. Single-
devices, providing a cost-effective solution for secure Small board computers such as Raspberry Pi provide a cost-effective
Office/Home Office (SOHO) environments. The obtained and energy-efficient platform capable of supporting
results indicate that ML techniques can effectively enhance networking services, local data processing, and ML inference
traffic visibility and support cybersecurity monitoring while [12]. Their low power consumption and flexibility make them
maintaining low resource consumption on Raspberry Pi-based attractive candidates for SOHO environments, where
platforms. affordable cybersecurity solutions are increasingly required
[1].
Keywords—VPN, Raspberry Pi, traffic analysis, traffic
classification, machine learning, Random Forest, Support Vector Despite the growing interest in VPN technologies and
Machine, TensorFlow Lite, edge computing, cybersecurity. ML-based traffic analysis, relatively few studies have
investigated the integration of secure VPN communication,
I. INTRODUCTION
real-time traffic monitoring, and intelligent traffic
The rapid growth of remote connectivity services, cloud- classification within a unified edge-computing framework.
based applications, and distributed computing environments Most existing approaches focus either on VPN deployment or
has significantly increased the demand for secure on traffic classification separately, without addressing the
communication mechanisms [1], [2]. VPNs have become one challenges associated with resource-constrained embedded
of the most widely adopted technologies for protecting data platforms [4].
confidentiality, ensuring secure remote access, and
To address this research gap, this paper proposes an
safeguarding sensitive information transmitted over public
intelligent VPN traffic analysis and classification framework
networks [3]. VPN solutions such as OpenVPN and
deployed on a Raspberry Pi platform. The proposed system
WireGuard provide encrypted communication channels that
integrates OpenVPN and WireGuard for secure
reduce the risk of eavesdropping, unauthorized access, and
communication, network traffic monitoring tools for packet
traffic manipulation [4].
acquisition, and ML techniques for traffic classification and
At the same time, the increasing volume and diversity of analysis. RF and SVM models are employed to identify and
network traffic have introduced new challenges for network categorize network traffic, while TensorFlow Lite is utilized
administrators and cybersecurity professionals [5]. Although to support lightweight real-time inference suitable for
VPN technologies successfully protect data confidentiality, embedded devices. The proposed framework aims to provide
they may also obscure traffic visibility, making the enhanced traffic visibility, improved cybersecurity monitoring
identification of network anomalies, malicious activities, and capabilities, and efficient operation in resource-constrained
traffic patterns more difficult [6]. Traditional traffic environments.
monitoring approaches often rely on manual inspection or
979-8-3315-5818-5/26/$31.00 ©2026 IEEE
09531611.6202.61096IACE/9011.01
:IOD
| EEEI
6202©
00.13$/62/5-8185-5133-8-979
|
)IACE(
ecnegilletnI
laicifitrA
dna
sretupmoC
,scinortcelE
no
ecnerefnoC
lanoitanretnI
ht81
6202
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on October 16,2026 at 16:36:48 UTC from IEEE Xplore. Restrictions apply.

The main contribution of this work consists in the investigated three architectures combining NN, Bidirectional
development of an intelligent VPN traffic analysis and Long Short-Term Memory (LSTM), RF, SVM, k-Nearest
classification framework deployed on a Raspberry Pi edge- Neighbors (k-NN), and ensemble voting techniques.
computing platform. The proposed system combines secure Experimental results showed that the first approach achieved
communication services provided through OpenVPN and the highest classification accuracy of 96.8%, while the second
WireGuard with real-time traffic monitoring and ML-based and third approaches achieved 95.2% and 96.5%,
analysis mechanisms. Furthermore, RF and SVM models are respectively. Furthermore, individual classifiers such as RF
integrated to perform network traffic classification, while and k-NN reached accuracies of 99.6% and 100% in specific
TensorFlow Lite enables lightweight inference suitable for configurations, demonstrating the effectiveness of hybrid ML
resource-constrained embedded environments. The models for encrypted traffic analysis. However, the study
framework was experimentally validated in a SOHO-oriented focused on application-level traffic classification and did not
scenario, demonstrating the feasibility of combining VPN address VPN deployment, real-time network monitoring, or
services, traffic monitoring, and intelligent analysis within a edge-based implementation on resource-constrained
unified low-cost platform. The obtained results highlight the platforms such as Raspberry Pi.
potential of edge-based ML techniques for enhancing traffic
Sattar et al. [15] proposed Encrypted Traffic Anomaly
visibility, supporting cybersecurity monitoring, and enabling
Detection using Self-Supervised Contrastive Learning (ET-
efficient network management in modern distributed
SSL), a privacy-preserving framework for anomaly detection
environments.
in encrypted network traffic. The method leverages self-
The remainder of this paper is organized as follows. supervised contrastive learning to extract discriminative
Section II presents the related work and background regarding representations from flow-level features, including packet
VPN technologies, edge computing platforms, and ML-based lengths, inter-arrival times, flow durations, and protocol
traffic analysis. Section III describes the proposed framework metadata, without requiring packet decryption or labeled
and system architecture. Section IV details the experimental datasets. Experimental evaluation on the Canadian Institute
setup and implementation methodology. Section V presents for Cybersecurity (CIC)-Darknet2020, Information Security
the obtained results and performance evaluation. Finally, Centre of Excellence (ISCX) VPN-nonVPN, and University
Section VI concludes the paper and outlines future research of New South Wales (UNSW)-NB15 datasets demonstrated
directions. classification accuracies of 96.8%, 94.3%, and 95.1%,
respectively, with false positive rates as low as 1.2%. The
II. RELATED WORK proposed approach also achieved a 92.7% true positive rate
The rapid evolution of cybersecurity threats, encrypted for zero-day attack detection, processing up to 10 Gbps of
communications, and edge computing technologies has encrypted traffic with a latency of 15-25 ms, making it suitable
stimulated extensive research efforts in the fields of network for real-time deployment. Furthermore, the framework
traffic analysis, intrusion detection, and intelligent monitoring outperformed conventional RF, K-Means, and Autoencoder-
systems. Recent studies have investigated various approaches based approaches in terms of accuracy, F1-score, and
based on ML, DL, and edge intelligence to improve network robustness against previously unseen attacks. However, the
visibility and support cybersecurity operations. Nevertheless, study focused on anomaly detection in encrypted traffic and
the integration of secure VPN communication, intelligent did not investigate VPN deployment architectures, network
traffic classification, and lightweight deployment on management strategies, or embedded implementations
embedded platforms remains an active research area. dedicated to secure remote access systems.
Razooqi and Pekar [13] proposed a wavelet-based ML Wijethilaka et al. [16] proposed a cost-effective ML-based
framework for binary VPN traffic detection, focusing on Network Intrusion Detection System (NIDS) deployed on a
distinguishing VPN-encrypted traffic from non-VPN Raspberry Pi 4 for real-time network traffic analysis. The
communications regardless of the underlying application. The framework combines multiple ML algorithms, including RF,
authors evaluated RF, Neural Networks (NN), and SVM using LSTM, Artificial NN (ANN), XGBoost, and Naïve Bayes, to
wavelet-derived temporal features extracted from network detect and classify a wide range of cyberattacks such as Denial
flows. Experimental results demonstrated that RF achieved of Service (DoS), Distributed DoS (DDoS), Structured Query
the best performance, reaching an F1-score of 99% and Language (SQL) Injection, Port Scanning, Malware,
maintaining 98% accuracy even after significant dataset Reconnaissance, Man-in-the-Middle (MitM), Brute Force,
filtering, while NN achieved an F1-score of 98% and SVM Ransomware, Worms, and Exploits. To address dataset
obtained a maximum F1-score of 90%. Furthermore, the study imbalance, the authors employed the Synthetic Minority
showed that deeper wavelet decomposition levels improved Oversampling Technique (SMOTE), significantly improving
classification performance, although the gains were relatively detection performance for minority attack classes. The system
small compared to the additional computational overhead. was implemented on a low-cost Raspberry Pi 4 platform and
However, the proposed approach focused exclusively on integrated with real-time alerting mechanisms including
binary VPN detection and did not investigate real-time traffic Light-Emitting Diodes (LEDs), buzzers, and email
monitoring, VPN service deployment, or lightweight edge notifications. Experimental evaluation on the NetFlow-
implementation on resource-constrained platforms such as University of Queensland-NIDS (NF-UQ-NIDS) dataset
Raspberry Pi. demonstrated a maximum detection accuracy of 96.5%, a
precision of 94.1%, a recall of 95.5%, and an F1-score of
Elmaghraby et al. [14] proposed a ML framework for
94.8% using the RF classifier. Furthermore, the proposed
encrypted network traffic classification, aiming to identify
NIDS achieved an average response time of approximately 50
different application categories, including web browsing,
ms, outperforming several traditional intrusion detection
Voice over Internet Protocol (VoIP), file transfer, and video
systems while maintaining low hardware costs. Although the
streaming, without decrypting packet contents. The authors
solution provides an effective and affordable approach for
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on October 16,2026 at 16:36:48 UTC from IEEE Xplore. Restrictions apply.

real-time network security monitoring, the study focuses network flows. These features include packet sizes, packet
primarily on intrusion detection and does not address VPN counts, flow duration, inter-arrival times, and protocol-
deployment, remote access architectures, or secure network specific information. The extracted features are then provided
tunneling mechanisms. to the ML engine, which employs RF and SVM classifiers to
identify traffic patterns and support intelligent network
Wang and Gu [17] proposed Parameter-Efficient Fine-
analysis.
Tuning-based Encrypted Traffic Representation Learning
Method (PETReLM), a DL framework designed for encrypted To enable efficient execution on resource-constrained
traffic classification in both network management and hardware, the trained ML models are optimized and deployed
cybersecurity scenarios. The proposed approach combines a using TensorFlow Lite. This approach reduces memory
Bidirectional Encoder Representations from Transformers consumption and computational overhead while preserving
(BERT)-based pre-trained model with a Parameter-Efficient classification performance. Finally, the generated results are
Fine-Tuning (PEFT) strategy using Low-Rank Adaptation displayed through a monitoring interface, allowing
(LoRA), significantly reducing the number of trainable administrators to observe traffic behavior and classification
parameters while maintaining high classification outcomes in real time.
performance. The framework processes encrypted traffic at
packet level, employing Byte-Pair Encoding and WordPiece
tokenization to transform packet payloads into sequences
suitable for transformer-based learning. The model is pre-
trained using Masked Language Modeling (MLM) and a
modified Next Sentence Prediction (mNSP) task, enabling the
extraction of generalized encrypted traffic representations.
Experimental validation was conducted on multiple public
datasets including ISCXVPN2016, ISCXTor2017, University
of Science and Technology of China - Traffic Flow
Classification (USTC-TFC2016), CIC-IDS2017, and CIC
Internet of Things (IoT) Dataset 2023. Results demonstrated Fig. 1. Overall architecture of the proposed VPN traffic analysis and
classification framework.
classification accuracies of up to 99.98% for Tor service
classification, 98.67% for VPN application classification, and
The proposed architecture enables the integration of secure
98.81% for malware traffic classification. Furthermore, the
VPN communication, traffic monitoring, and ML-based
proposed framework reduced the trainable parameter count to
analysis within a single embedded platform. Unlike
approximately 5.6% of the Encrypted Traffic (ET)-BERT
conventional solutions that treat these functions
model while decreasing training time by 16.68% and reducing
independently, the proposed framework provides a unified
Graphics Processing Unit (GPU) memory consumption. The
and cost-effective approach for intelligent network monitoring
study highlights the potential of transformer-based
and cybersecurity support at the network edge.
architectures combined with parameter-efficient adaptation
techniques for scalable encrypted traffic analysis in modern B. VPN Communication Layer
cybersecurity environments.
The VPN communication layer represents the security
foundation of the proposed framework, presented in Fig. 2,
III. PROPOSED FRAMEWORK
providing encrypted communication channels between remote
A. System Architecture clients and the Raspberry Pi edge platform. To ensure secure
data transmission and support different operational
The proposed framework (shown in Fig. 1) was designed
requirements, two widely adopted VPN technologies, namely
to provide secure communication, real-time traffic
OpenVPN and WireGuard, were integrated into the system
monitoring, and intelligent traffic classification within a
architecture.
unified edge-computing environment. The system combines
VPN technologies, traffic analysis mechanisms, and ML OpenVPN was selected due to its maturity, extensive
algorithms deployed on a Raspberry Pi platform. The primary protocol support, and strong security mechanisms based on
objective is to enhance network visibility and cybersecurity Secure Sockets Layer/Transport Layer Security (SSL/TLS)
monitoring while maintaining low hardware costs and reduced encryption. The protocol enables the establishment of secure
computational requirements suitable for SOHO environments. tunnels over public networks while supporting authentication,
encryption, and integrity verification services. Furthermore,
The overall architecture consists of five main components:
its widespread adoption in enterprise and remote-access
the VPN communication layer, the traffic monitoring module,
environments makes it a suitable candidate for secure
the feature extraction module, the ML classification engine,
communication infrastructures [18].
and the result visualization module. The VPN communication
layer establishes secure communication channels using In parallel, WireGuard was incorporated as a lightweight
OpenVPN and WireGuard protocols, ensuring confidentiality alternative designed to provide reduced computational
and integrity of transmitted data. Network traffic generated overhead and improved communication efficiency. Unlike
through these secure tunnels is continuously monitored and traditional VPN solutions, WireGuard employs a simplified
collected by the traffic monitoring module, which captures architecture and a modern cryptographic suite, enabling faster
packet-level and flow-level information required for further connection establishment and lower latency. These
analysis. characteristics make it particularly attractive for embedded
and edge-computing environments where computational
The collected traffic data are subsequently processed by
resources are limited [19].
the feature extraction module, where relevant statistical and
temporal characteristics are derived from the captured
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on October 16,2026 at 16:36:48 UTC from IEEE Xplore. Restrictions apply.

Within the proposed framework, remote clients establish  enables ML algorithms to identify traffic patterns, distinguish
encrypted  tunnels  with  the  Raspberry  Pi  VPN  gateway  communication  behaviors,  and  support  real-time
| through  | either  | OpenVPN  | or  | WireGuard.  | All  | transmitted  |     |     |     |     |     |     |     |
| -------- | ------- | -------- | --- | ----------- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- |
cybersecurity monitoring on the Raspberry Pi platform.
traffic is routed through the secure communication channel
| before reaching  |              | the protected  |                  | network         | environment. This  |             |     |     |     |     |     |     |     |
| ---------------- | ------------ | -------------- | ---------------- | --------------- | ------------------ | ----------- | --- | --- | --- | --- | --- | --- | --- |
| approach         | ensures      | the            | confidentiality  |                 | and                | integrity   | of  |     |     |     |     |     |     |
| exchanged        | information  |                | while            | simultaneously  |                    | generating  |     |     |     |     |     |     |     |
encrypted traffic suitable for monitoring and classification
purposes.

Fig. 3.
Captured VPN traffic visualization using Wireshark during the
monitoring stage.
  D. Feature Extraction and Traffic Representation
Fig. 2.  VPN communication workflow implemented on the Raspberry Pi  The effectiveness of ML algorithms largely depends on the
platform.
quality and relevance of the extracted traffic features. Since
VPN technologies encrypt the packet payload, direct content
The integration of both VPN technologies enables the
|     |     |     |     |     |     |     |     | inspection  | is  not  | feasible.  | Consequently,  | the  | proposed  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | ---------- | -------------- | ---- | --------- |
evaluation of traffic characteristics under different encryption
framework relies on statistical and flow-based characteristics
| mechanisms  | while  | maintaining  |     | a  secure  |     | communication  |     |     |     |     |     |     |     |
| ----------- | ------ | ------------ | --- | ---------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
that can be obtained from captured network traffic without
environment. The generated traffic serves as the primary input
violating the confidentiality provided by the VPN tunnel.
for the monitoring and ML modules described in the following
sections.  After packet acquisition, the monitoring module processes
the captured traffic and extracts a set of descriptive features
C. Traffic Monitoring and Data Collection
from each communication flow. These features are selected to
The traffic monitoring module is responsible for capturing  characterize the behavior of network sessions while remaining
and observing the network packets generated through the VPN
independent of the encrypted packet contents. The extracted
communication layer. After the VPN tunnel is established, the
attributes include packet length, flow duration, packet count,
Raspberry Pi operates as an intermediate edge node that routes
|     |     |     |     |     |     |     |     | transmitted  | bytes,  | source  | and  | destination  | ports,  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------- | ------- | ---- | ------------ | ------- |
the client traffic and enables local packet inspection without  communication protocol, and packet inter-arrival times.
| interrupting  | the  | secure  | communication  |     |     | process.  | This  |     |     |     |     |     |     |
| ------------- | ---- | ------- | -------------- | --- | --- | --------- | ----- | --- | --- | --- | --- | --- | --- |
configuration allows the system to collect relevant traffic  The extracted parameters are subsequently organized into
information while preserving the encrypted nature of the  feature  vectors  that  provide  a  compact  numerical
transmitted data.  representation  of  each  observed  traffic  flow.  This
representation enables the ML models to identify similarities
Traffic acquisition was performed using packet capture  and differences between traffic patterns generated by various
tools  such  as  Wireshark  (Fig.  3)  and  command-line  network  activities.  Furthermore,  the  use  of  flow-based
monitoring utilities. These tools enable the visualization and
|     |     |     |     |     |     |     |     | features  | reduces  computational  |     | complexity  | and  | facilitates  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------------------- | --- | ----------- | ---- | ------------ |
extraction of packet-level information, including source and
|              |             |     |            |            |     |         |          | deployment  | on  resource-constrained  |     | embedded  |     | platforms  |
| ------------ | ----------- | --- | ---------- | ---------- | --- | ------- | -------- | ----------- | ------------------------- | --- | --------- | --- | ---------- |
| destination  | addresses,  |     | transport  | protocol,  |     | packet  | length,  |             |                           |     |           |     |            |
such as Raspberry Pi, as shown in Fig. 4.
timestamps, and communication direction. Such information
|                |      |               |     |               |      |       |          | Before being supplied to the classification  |     |     |     |     | stage, the  |
| -------------- | ---- | ------------- | --- | ------------- | ---- | ----- | -------- | -------------------------------------------- | --- | --- | --- | --- | ----------- |
| is  essential  | for  | constructing  |     | the  feature  | set  | used  | by  the  |                                              |     |     |     |     |             |
subsequent ML classification stage.  extracted  features  undergo  preprocessing  operations  to
improve data quality and ensure consistent model behavior.
The collected traffic data are not analyzed based on
These operations include data normalization, removal of
| packet  | payload  | inspection,  |     | since  | VPN  communication  |     |     |     |     |     |     |     |     |
| ------- | -------- | ------------ | --- | ------ | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
incomplete records, and formatting procedures required by
| encrypts  | the  transmitted  |     | content.  | Instead,  |     | the  proposed  |     |     |     |     |     |     |     |
| --------- | ----------------- | --- | --------- | --------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
the ML framework. The resulting feature vectors constitute
framework relies on metadata and statistical characteristics
the input data used by the RF and SVM classifiers described
extracted from the observed traffic flows. This approach is
in the following section.
suitable for encrypted environments, where direct content
The adopted feature extraction strategy enables efficient
inspection is either technically impractical or undesirable
analysis of encrypted traffic while preserving user privacy.
from a privacy perspective.  By focusing exclusively on traffic metadata and statistical
The monitoring process therefore provides the connection
characteristics, the proposed framework remains applicable
| between         | the  | VPN      | infrastructure  |               | and  the  | intelligent  |         |               |          |            |            |                |            |
| --------------- | ---- | -------- | --------------- | ------------- | --------- | ------------ | ------- | ------------- | -------- | ---------- | ---------- | -------------- | ---------- |
|                 |      |          |                 |               |           |              |         | to  both      | OpenVPN  | and        | WireGuard  | communication  |            |
| classification  |      | module.  | By              | transforming  |           | raw          | packet  |               |          |            |            |                |            |
|                 |      |          |                 |               |           |              |         | environments  | without  | requiring  | access     | to  the        | encrypted  |
observations into structured traffic descriptors, the system
payload contents.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on October 16,2026 at 16:36:48 UTC from IEEE Xplore.  Restrictions apply.

Fig. 4.  Feature extraction process used for traffic representation and ML analysis.

E. ML-Based Traffic Classification

As illustrated in Fig. 5, the extracted traffic features were  classes.  By  projecting  the  feature  vectors  into  a  higher-
analyzed using supervised ML algorithms to identify traffic
dimensional space, SVM can effectively distinguish between
patterns and support intelligent network monitoring. Among  traffic categories that are not linearly separable in the original
the  numerous  classification  techniques  available  in  the  feature  space.  This  characteristic  makes  the  algorithm
literature, RF and SVM were selected due to their proven  particularly suitable for traffic classification tasks involving
effectiveness in network traffic analysis, robustness against  encrypted communications [21].
| noisy  data,  | and  | suitability  | for  | deployment  | on  resource- |     |     |     |     |     |     |     |
| ------------- | ---- | ------------ | ---- | ----------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
The SVM classifier was implemented using a Radial Basis
constrained edge platforms.
|     |     |     |     |     |     |     | Function  | (RBF)  kernel  | to  | model  non-linear  |     | relationships  |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------------- | --- | ------------------ | --- | -------------- |
RF is an ensemble learning method that combines multiple  within the extracted traffic features. To improve classification
decision trees to improve classification accuracy and reduce  performance,  hyperparameter  optimization  was  performed
overfitting. During the training process, each decision tree is
|     |     |     |     |     |     |     | through  | GridSearchCV,  | exploring  | different  | values  | of  the  |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------------- | ---------- | ---------- | ------- | -------- |
constructed using a randomly selected subset of features and
regularization parameter C and kernel coefficient gamma.
training samples. The final classification result is obtained  Furthermore, stratified sampling was applied during dataset
through  majority  voting  among  all  generated  trees.  This  partitioning to preserve class distributions across training and
approach enables the model to capture complex relationships  testing subsets. The SVM algorithm was selected due to its
within the traffic data while maintaining high generalization  strong capability to identify optimal decision boundaries in
capability [20].
high-dimensional feature spaces and its proven effectiveness
in network traffic classification tasks.
The RF classifier was employed as an ensemble learning
technique for network traffic classification. The model was  Both  classifiers  receive  the  feature  vectors  generated
configured using 200 decision trees, allowing the classifier to  during the extraction stage and produce traffic classification
| improve      | robustness  | and       | reduce       | overfitting  | through          | the  |                 |           |          |              |          |                 |
| ------------ | ----------- | --------- | ------------ | ------------ | ---------------- | ---- | --------------- | --------- | -------- | ------------ | -------- | --------------- |
|              |             |           |              |              |                  |      | outputs  based  | on  the   | learned  | patterns.    | The      | classification  |
| aggregation  | of          | multiple  | independent  |              | decision-making  |      |                 |           |          |              |          |                 |
|              |             |           |              |              |                  |      | results  can    | be  used  | to       | distinguish  | between  | different       |
processes. Prior to training, feature selection was performed  communication  behaviors,  identify  traffic  categories,  and
using correlation analysis, retaining the most relevant traffic  support  real-time  network  monitoring.  Furthermore,  the
attributes  with  respect  to  the  target  protocol  class.  The  simultaneous evaluation of RF and SVM allows a comparative
resulting feature vectors were standardized and subsequently
analysis of their performance within the proposed VPN traffic
used for model training and evaluation. The adoption of
analysis framework [22].
Random Forest was motivated by its ability to handle high-
|              |          |        |          |         |                 |     | The       | adoption  of  | these    | ML  techniques  |          | enables  the  |
| ------------ | -------- | ------ | -------- | ------- | --------------- | --- | --------- | ------------- | -------- | --------------- | -------- | ------------- |
| dimensional  | traffic  | data,  | provide  | strong  | generalization  |     |           |               |          |                 |          |               |
|              |          |        |          |         |                 |     | proposed  | system  to    | perform  | intelligent     | traffic  | analysis      |
performance, and maintain stable classification accuracy in
complex network environments.  without  requiring  access  to  encrypted  packet  contents.
Consequently, the framework preserves the privacy benefits
SVM represents  another  widely  adopted classification  provided  by  VPN  technologies  while  still  maintaining
technique for network security applications. The algorithm
|           |               |     |          |           |           |       | visibility  | into  network  | behavior  | through  | metadata-based  |     |
| --------- | ------------- | --- | -------- | --------- | --------- | ----- | ----------- | -------------- | --------- | -------- | --------------- | --- |
| attempts  | to  identify  | an  | optimal  | decision  | boundary  | that  |             |                |           |          |                 |     |
analysis.
maximizes the separation margin between different traffic

Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on October 16,2026 at 16:36:48 UTC from IEEE Xplore.  Restrictions apply.

Fig. 5.  ML-based traffic classification process using RF and SVM models.
| F. TensorFlow Lite Edge Deployment  |     |     |     |     |     |     |     |     |     |     |
| ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
process reduces model size while preserving the classification
| To  enable  | efficient  |     | execution  | on  resource-constrained  |     |     |     |     |     |     |
| ----------- | ---------- | --- | ---------- | ------------------------- | --- | --- | --- | --- | --- | --- |
capabilities required for real-time traffic analysis. As a result,
| hardware,  | the  proposed  |     | framework  | (Fig.  | 6)  incorporates  |     |     |     |     |     |
| ---------- | -------------- | --- | ---------- | ------ | ----------------- | --- | --- | --- | --- | --- |
TensorFlow Lite as the inference engine for ML deployment  the  proposed  framework  can  perform  intelligent  traffic
on the Raspberry Pi platform. TensorFlow Lite is specifically  classification  locally  without  relying  on  external  cloud
services or remote processing infrastructure.
| designed  | for embedded  |     | and  edge-computing  |     | applications,  |     |     |     |     |     |
| --------- | ------------- | --- | -------------------- | --- | -------------- | --- | --- | --- | --- | --- |
providing  reduced  memory  consumption,  lower  The deployment architecture enables the Raspberry Pi to
computational  requirements,  and  improved  inference  simultaneously  perform  VPN  services, traffic  monitoring,
| performance  | compared  |     | to  conventional  |     | ML  deployment  |          |              |          |            |                    |
| ------------ | --------- | --- | ----------------- | --- | --------------- | -------- | ------------ | -------- | ---------- | ------------------ |
|              |           |     |                   |     |                 | feature  | extraction,  | and  ML  | inference  | within  a  single  |
frameworks [23].
|     |     |     |     |     |     | embedded  | platform.  | This  | integration  | minimizes  |
| --- | --- | --- | --- | --- | --- | --------- | ---------- | ----- | ------------ | ---------- |
communication latency and improves system responsiveness,
After the training phase, the developed ML models are
|     |     |     |     |     |     | making  | the  solution  | suitable  | for  real-time  | cybersecurity  |
| --- | --- | --- | --- | --- | --- | ------- | -------------- | --------- | --------------- | -------------- |
converted into lightweight formats suitable for execution on
monitoring applications.
| the  Raspberry  |     | Pi  | device.  | This  | optimization   |     |     |     |     |     |
| --------------- | --- | --- | -------- | ----- | -------------- | --- | --- | --- | --- | --- |

Fig. 6.  TensorFlow Lite deployment workflow on the Raspberry Pi platform.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on October 16,2026 at 16:36:48 UTC from IEEE Xplore.  Restrictions apply.

By executing the inference process locally, the framework  based  analysis  on  a  low-cost  embedded  platform.
also improves data privacy, since captured traffic information  Consequently, the proposed framework provides a practical
remains  within  the  monitored  environment.  Furthermore,  solution  for  SOHO  environments  that  require  secure
local processing reduces network overhead and eliminates the  communication,  traffic  visibility,  and  lightweight
dependency  on  continuous  Internet  connectivity  for  cybersecurity capabilities.
classification tasks.
IV. EXPERIMENTAL RESULTS AND DISCUSSION
| To  support  |     | real-time  | inference  | on  | the  Raspberry  |     | Pi  |     |     |     |     |     |     |     |
| ------------ | --- | ---------- | ---------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
platform,  a  lightweight  neural  network  was  implemented  A. Experimental Setup
using TensorFlow and subsequently converted to TensorFlow  The  experimental  evaluation  was  conducted  using  a
Lite format. The architecture consisted of two fully connected  Raspberry Pi 5 platform configured as an edge-computing
hidden layers containing 128 and 64 neurons respectively,  node capable of providing VPN services, traffic monitoring
employing Rectified Linear Unit (ReLU) activation functions  functionality, and ML-based traffic analysis. The hardware
and a dropout rate of 0.3 to mitigate overfitting. Model
|     |     |     |     |     |     |     |     | platform  | was  selected  | due  | to  | its  low  | cost,  | low  power  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------------- | ---- | --- | --------- | ------ | ----------- |
training  was  performed  using  the  Adam  optimizer  and  consumption,  and  suitability  for  SOHO  cybersecurity
categorical  cross-entropy  loss  function  over  ten  training  deployments.  The  experimental  environment  integrated
epochs. Following the training stage, the model was converted  OpenVPN and WireGuard services, allowing encrypted traffic
to TensorFlow Lite with optimization and float16 quantization  to  be  generated  and  monitored  under  realistic  operating
| enabled,  | reducing  | memory  |     | requirements  | and  | improving  |     |              |      |            |     |           |                 |     |
| --------- | --------- | ------- | --- | ------------- | ---- | ---------- | --- | ------------ | ---- | ---------- | --- | --------- | --------------- | --- |
|           |           |         |     |               |      |            |     | conditions.  | The  | Raspberry  | Pi  | platform  | simultaneously  |     |
execution efficiency on the embedded platform.  performed  packet  acquisition,  feature  extraction,  traffic
|              |           |            |             |                |               |            |      | classification,  | and            | real-time  | inference  |     | tasks.      | The  overall  |
| ------------ | --------- | ---------- | ----------- | -------------- | ------------- | ---------- | ---- | ---------------- | -------------- | ---------- | ---------- | --- | ----------- | ------------- |
| The          | adoption  | of         | TensorFlow  | Lite           | demonstrates  |            | the  |                  |                |            |            |     |             |               |
|              |           |            |             |                |               |            |      | experimental     | configuration  |            | employed   |     | throughout  | the           |
| feasibility  | of        | combining  | VPN         | communication  |               | services,  |      |                  |                |            |            |     |             |               |
evaluation process is illustrated in Fig. 7.
| network  | traffic  | monitoring,  |     | and  | intelligent  |     | ML-  |     |     |     |     |     |     |     |
| -------- | -------- | ------------ | --- | ---- | ------------ | --- | ---- | --- | --- | --- | --- | --- | --- | --- |

Fig. 7.  Experimental setup used for VPN traffic acquisition, ML model training, and edge-based inference on the Raspberry Pi platform.
The  software  environment  consisted  of  Raspberry  Pi  the central node for VPN communication, traffic monitoring,
Operating System (OS) (64-bit), OpenVPN 2.6, WireGuard  ML inference, and real-time network analysis.
| 1.0,  Wireshark/tshark  |        |      | 4.2,  Python  | 3.11,  | Scikit-learn  |     | 1.5,     |                 |            |               |              |           |                    |               |
| ----------------------- | ------ | ---- | ------------- | ------ | ------------- | --- | -------- | --------------- | ---------- | ------------- | ------------ | --------- | ------------------ | ------------- |
|                         |        |      |               |        |               |     |          | Representative  |            | measurements  |              | obtained  |                    | during  live  |
| TensorFlow              | 2.16,  | and  | TensorFlow    |        | Lite  2.16.   |     | Traffic  |                 |            |               |              |           |                    |               |
|                         |        |      |               |        |               |     |          | operation       | indicated  | a  CPU        | utilization  |           | of  approximately  |               |
monitoring was performed directly on the VPN interfaces,
|     |     |     |     |     |     |     |     | 21.6%,  | memory  | utilization  | of  | 35.1%,  | and  | a  processor  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ------------ | --- | ------- | ---- | ------------- |
enabling the collection of network flow information from
|     |     |     |     |     |     |     |     | temperature  | of  | about  40°C,  | while  | maintaining  |     | network  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------------- | ------ | ------------ | --- | -------- |
encrypted communication sessions. Captured traffic data were
throughput levels of 2.26 Mbps (transmit) and 2.37 Mbps
subsequently exported and processed using dedicated ML
|     |     |     |     |     |     |     |     | (receive).  | No  stability  | issues  |     | were  observed  |     | during  the  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------------- | ------- | --- | --------------- | --- | ------------ |
pipelines developed for the proposed framework.
experimental campaign, confirming the practical feasibility of
The experimental platform was based on a Raspberry Pi 5  deploying  intelligent  VPN  traffic  monitoring  and
equipped with a quad-core 64-bit Advanced RISC (Reduced  classification services on low-cost edge-computing platforms
Instruction  Set  Computer)  Machines  (Arm)  Cortex-A76  intended for SOHO cybersecurity applications.
processor operating at 2.4 GHz, 2 GB Low Power Double
For the ML experiments, the publicly available Internet
| Data  Rate  | (LPDDR4X)  |     |     | memory,  | Gigabit  | Ethernet  |     |           |                |     |          |        |          |           |
| ----------- | ---------- | --- | --- | -------- | -------- | --------- | --- | --------- | -------------- | --- | -------- | ------ | -------- | --------- |
|             |            |     |     |          |          |           |     | Protocol  | (IP)  Network  |     | Traffic  | Flows  | Labeled  | with  87  |
connectivity, and Raspberry Pi OS [24]. The device served as
Applications dataset was employed [25]. This dataset contains
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on October 16,2026 at 16:36:48 UTC from IEEE Xplore.  Restrictions apply.

labeled  network  traffic  flows  associated  with  many  (cid:8)(cid:9)+(cid:8)(cid:11)
|     |     |     |     |     |     |     |     |     | (cid:1)(cid:2)(cid:2)(cid:3)(cid:4)(cid:5)(cid:2)(cid:6) |     | =   |     |     |     | (cid:14)1(cid:16)  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------------- | --- | --- | --- | --- | --- | ------------------ |
applications and communication services, making it suitable
(cid:8)(cid:9)+(cid:8)(cid:11)+(cid:12)(cid:9)+(cid:12)(cid:11)
for evaluating traffic classification algorithms under realistic
conditions. During the experimental phase, approximately  where TP denotes true positives, TN true negatives, FP false
50,000 traffic flow records were processed and analyzed for  positives, and FN false negatives [26].
training and testing purposes.
Prior  to  model  training,  the  dataset  underwent  a  Although accuracy provides a global assessment of model
preprocessing stage that included the removal of incomplete  performance, it may not fully reflect the classifier behavior
|     |     |     |     |     |     |     |     | when  dealing  |     | with  | multiple  | traffic  | classes.  | Therefore,  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----- | --------- | -------- | --------- | ----------- | --- |
records, elimination of irrelevant attributes, label encoding of
protocol  classes,  and  feature  normalization  using  the  Precision  was  also  considered.  Precision  measures  the
StandardScaler  method.  Additionally,  correlation-based  proportion of correctly identified positive instances among all
feature selection was applied to identify the most informative  samples classified as positive [26] (2):
traffic characteristics and reduce data dimensionality while
preserving  classification  performance.  This  procedure  (cid:8)(cid:9)
|              |     |            |     |                    |     |      |           |     |     | (cid:9)(cid:4)(cid:17)(cid:2)(cid:18)(cid:19)(cid:18)(cid:20)(cid:21) |     | =   |     |     | (cid:14)2(cid:16)  |
| ------------ | --- | ---------- | --- | ------------------ | --- | ---- | --------- | --- | --- | --------------------------------------------------------------------- | --- | --- | --- | --- | ------------------ |
| contributed  | to  | improving  |     | model  efficiency  |     | and  | reducing  |     |     |                                                                       |     |     |     |     |                    |
(cid:8)(cid:9)+(cid:12)(cid:9)
computational overhead during the training and inference
stages.
|     |     |     |     |     |     |     |     | A  high   | precision  |         | value  | indicates  | that         | the  classifier  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | ------- | ------ | ---------- | ------------ | ---------------- | --- |
|     |     |     |     |     |     |     |     | produces  | a  low     | number  | of     | false      | alarms  and  | incorrectly      |     |
The dataset was divided into training and testing subsets
using  an  80%-20%  partitioning  strategy.  For  the  SVM  classified traffic flows. Another important metric is Recall,
implementation, stratified sampling was employed to preserve  which quantifies the ability of the classifier to correctly
class distributions across both subsets and ensure a balanced  identify all relevant traffic instances belonging to a specific
evaluation process. The RF classifier was configured using
class [26] (3):
200 decision trees, while the SVM model employed a RBF
kernel  optimized  through  a  GridSearchCV  procedure.  In  (cid:8)(cid:9)
|            |                 |     |         |          |               |     |      |     |     | (cid:23)(cid:17)(cid:2)(cid:5)(cid:24)(cid:24) | =   |     |     |     | (cid:14)3(cid:16)  |
| ---------- | --------------- | --- | ------- | -------- | ------------- | --- | ---- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- | ------------------ |
| parallel,  | a  lightweight  |     | neural  | network  | architecture  |     | was  |     |     |                                                |     |     |     |     |                    |
(cid:8)(cid:9)+(cid:12)(cid:11)
implemented using TensorFlow, consisting of two hidden
layers with 128 and 64 neurons, respectively, followed by
|     |     |     |     |     |     |     |     | Recall  | is  | particularly  |     | relevant  | in  | cybersecurity  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | ------------- | --- | --------- | --- | -------------- | --- |
conversion into TensorFlow Lite format for deployment on
applications, where the failure to identify a specific traffic
the Raspberry Pi platform.
category may reduce the effectiveness of the monitoring
Model performance was evaluated using widely adopted  system. To provide a balanced evaluation that simultaneously
classification metrics, including Accuracy, Precision, Recall,  considers  both  Precision  and  Recall,  the  F1-score  was
and F1-score. Furthermore, confusion matrices and detailed
|                 |     |          |       |            |     |          |     | employed.  | This  | metric  | represents  |     | the  harmonic  |     | mean  |
| --------------- | --- | -------- | ----- | ---------- | --- | -------- | --- | ---------- | ----- | ------- | ----------- | --- | -------------- | --- | ----- |
| classification  |     | reports  | were  | generated  | to  | provide  | a   |            |       |         |             |     |                |     |       |
between Precision and Recall and is defined as [26] (4):
| comprehensive  |     | assessment  |     | of  the  | traffic  | classification  |     |     |     |     |     |     |     |     |     |
| -------------- | --- | ----------- | --- | -------- | -------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
capabilities of the implemented models. The experimental  (cid:9)(cid:4)(cid:17)(cid:2)(cid:18)(cid:19)(cid:18)(cid:20)(cid:21)⋅(cid:23)(cid:17)(cid:2)(cid:5)(cid:24)(cid:24)
evaluation  also  considered  the  practical  feasibility  of  (cid:12)1=2⋅ (cid:14)4(cid:16)
(cid:9)(cid:4)(cid:17)(cid:2)(cid:18)(cid:19)(cid:18)(cid:20)(cid:21)+(cid:23)(cid:17)(cid:2)(cid:5)(cid:24)(cid:24)
deploying ML-based traffic analysis on a low-cost embedded
| platform,  | focusing  |              | on  the  | ability  to  | perform  | real-time      |     |      |           |     |             |         |       |            |     |
| ---------- | --------- | ------------ | -------- | ------------ | -------- | -------------- | --- | ---- | --------- | --- | ----------- | ------- | ----- | ---------- | --- |
|            |           |              |          |              |          |                |     | The  | F1-score  | is  | especially  | useful  | when  | comparing  |     |
| inference  | while     | maintaining  |          | acceptable   |          | computational  |     |      |           |     |             |         |       |            |     |
classifiers operating on datasets containing multiple traffic
resource utilization.
categories and varying class distributions.
| The  | adopted  | experimental  |     | setup  | provides  | a   | realistic  |     |     |     |     |     |     |     |     |
| ---- | -------- | ------------- | --- | ------ | --------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
In addition to these numerical metrics, confusion matrices
| environment  | for  | validating  |     | the  proposed  | intelligent  |     | VPN  |     |     |     |     |     |     |     |     |
| ------------ | ---- | ----------- | --- | -------------- | ------------ | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
and detailed classification reports were generated for each
traffic  analysis  framework.  By  combining  secure  VPN  evaluated  model.  These  tools  provide  class-level
communication, traffic monitoring, ML-based classification,  performance information and facilitate the identification of
and edge deployment within a unified Raspberry Pi platform,
traffic categories that may be more difficult to distinguish.
| the  experimental  |     | configuration  |     | enables  | a   | comprehensive  |     |     |     |     |     |     |     |     |     |
| ------------------ | --- | -------------- | --- | -------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
The combination of Accuracy, Precision, Recall, F1-score,
evaluation of both classification performance and practical
|     |     |     |     |     |     |     |     | and  confusion  |     | matrix  | analysis  | provide  | a   | comprehensive  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------- | --------- | -------- | --- | -------------- | --- |
deployment feasibility in real-world networking scenarios.
framework for evaluating the effectiveness of the proposed
B. Performance Evaluation Metrics
intelligent VPN traffic classification system.
To assess the effectiveness of the proposed VPN traffic  C. Classification Results
| classification  |     | framework,  |     | several  widely  |     | adopted  | ML  |     |     |     |     |     |     |     |     |
| --------------- | --- | ----------- | --- | ---------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
The proposed ML framework was evaluated using three
evaluation metrics were employed. These metrics provide a
classification approaches, namely RF, SVM, and TensorFlow
comprehensive assessment of the classification performance
Lite-based neural network inference. The experiments were
and enable a detailed comparison between the implemented
|     |     |     |     |     |     |     |     | conducted  | using  | the  | preprocessed  |     | network  | traffic  | dataset  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | ---- | ------------- | --- | -------- | -------- | -------- |
RF, SVM, and TensorFlow Lite-based models.
described in the previous section, while the evaluation was
The primary performance indicator used in this study is  performed using Accuracy, Precision, Recall, and F1-score
| Accuracy,  | which  | represents  |     | the  proportion  |     | of  | correctly  | metrics.  |     |     |     |     |     |     |     |
| ---------- | ------ | ----------- | --- | ---------------- | --- | --- | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- |
classified traffic instances relative to the total number of
Prior to model training, an exploratory analysis of the
analyzed samples. Accuracy provides an overall measure of
dataset was performed to investigate the distribution of traffic
classification effectiveness [26] and is defined as (1):
classes and the characteristics of the extracted network flows.
The employed dataset contains approximately 50,000 traffic
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on October 16,2026 at 16:36:48 UTC from IEEE Xplore.  Restrictions apply.

records described by 87 traffic-related attributes and multiple To improve classification efficiency and reduce
application categories, including Hypertext Transfer Protocol computational complexity, a feature-selection stage was
(HTTP), SSL, GOOGLE, AMAZON, YOUTUBE, applied. Correlation analysis was initially performed to
MICROSOFT, and WINDOWS_UPDATE traffic. The identify dependencies among the extracted traffic
distribution of the analyzed traffic classes is presented in Fig. 8. characteristics. Subsequently, the most relevant 29 features
were selected and retained for model training. The resulting
feature correlation matrix is illustrated in Fig. 9.
The RF classifier achieved strong classification
performance across all evaluated traffic categories. The initial
evaluation resulted in an overall classification accuracy of
approximately 92.33%, while most application classes
obtained F1-score values exceeding 0.90. As illustrated in Fig.
10, the classifier demonstrated particularly good performance
for HTTP, MICROSOFT, SSL, and WINDOWS_UPDATE
traffic classes.
The confusion matrix associated with the Random Forest
model is presented in Fig. 11. Most samples are concentrated
along the main diagonal, indicating successful classification
of most traffic flows. Only a limited number of
misclassifications were observed between traffic categories
exhibiting similar communication characteristics.
Fig. 8. Overview of the network traffic dataset containing 50,000 traffic
flows and multiple application classes used for training and evaluation.
Fig. 9. Correlation heatmap of the 29 most relevant traffic features selected for classification.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on October 16,2026 at 16:36:48 UTC from IEEE Xplore. Restrictions apply.

The SVM classifier was also evaluated using the same
dataset and feature set. The obtained confusion matrix, shown
in Fig. 13, indicates that the model successfully identified
most traffic categories. Nevertheless, a higher number of
classification errors can be observed when compared with the
Random Forest approach, particularly for traffic classes
exhibiting similar statistical characteristics.
Fig. 10. RF classification report obtained on the original dataset.
Fig. 13. Confusion matrix obtained using the SVM classifier.
To investigate the feasibility of edge-based deployment, a
lightweight neural network model was implemented and
converted to TensorFlow Lite format. During training, both
training and validation accuracy increased steadily over
successive epochs, demonstrating successful convergence of
the learning process. The corresponding training evolution is
illustrated in Fig. 14.
Fig. 11. Confusion matrix obtained using the RF classifier.
After applying feature optimization and parameter tuning
procedures, the RF model achieved a significantly improved
performance (Fig. 12), reaching an overall classification
accuracy of 98.46%. Furthermore, the weighted F1-score
exceeded 0.98, demonstrating the effectiveness of the selected
feature subset and confirming the suitability of ensemble-
learning methods for VPN traffic analysis and application
identification.
Fig. 14. TensorFlow Lite training and validation accuracy evolution during
model training.
The TensorFlow Lite model achieved a final classification
accuracy of 90.98% and an F1-score of 0.8958. Although its
classification performance was slightly lower than that
obtained by the Random Forest classifier, the model provides
an attractive solution for embedded and edge-computing
environments due to its reduced computational requirements
and efficient inference capabilities.
Finally, the developed framework was validated in a real-
time monitoring scenario executed directly on the Raspberry
Pi platform. The system successfully identified and classified
multiple traffic categories, including SSL, GOOGLE,
Fig. 12. Improved RF classification performance after feature optimization.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on October 16,2026 at 16:36:48 UTC from IEEE Xplore. Restrictions apply.

YOUTUBE, and HTTP_PROXY flows during live network proposed framework to perform intelligent traffic monitoring
operation. An example of the real-time traffic classification under practical operating conditions.
results is presented in Fig. 15, confirming the capability of the
Fig. 15. Real-time traffic classification results obtained during live network monitoring.
The obtained results demonstrate that ML techniques can traffic classification can also be performed directly on
effectively classify encrypted and application-level network embedded edge devices with limited computational resources.
traffic using statistical flow characteristics without requiring
The obtained results confirm the effectiveness of statistical
access to packet payload contents. Among the evaluated
traffic features for identifying application-level
approaches, the Random Forest classifier achieved the highest
communication patterns, even when traffic is protected by
overall performance, while the TensorFlow Lite
VPN encryption mechanisms. Furthermore, the successful
implementation provided an effective compromise between
deployment of the classification framework on Raspberry Pi
classification accuracy and deployment feasibility on
demonstrates the feasibility of implementing intelligent
resource-constrained edge devices.
cybersecurity services on low-cost hardware platforms
V. CONCLUSION suitable for SOHO environments and edge-computing
scenarios.
This paper presented an intelligent VPN traffic analysis
and classification framework implemented on a Raspberry Pi Future research directions include the investigation of DL
edge-computing platform using ML techniques. The proposed architectures specifically designed for encrypted traffic
solution integrates secure VPN communication, real-time analysis, the integration of anomaly and intrusion detection
traffic monitoring, feature extraction, and intelligent traffic mechanisms, and the evaluation of the proposed framework
classification within a unified architecture designed for under larger-scale network environments. Additional work
resource-constrained environments. By combining OpenVPN will also focus on improving real-time inference performance
and WireGuard services with ML-based analysis, the and extending the system to support adaptive and
framework enables enhanced visibility into encrypted network continuously updated ML models capable of responding to
traffic without requiring access to packet payload contents. emerging network threats and evolving traffic patterns.
Three ML approaches were evaluated, namely RF, SVM, The proposed framework demonstrates that the
and TensorFlow Lite-based neural network inference. combination of VPN technologies, edge computing, and ML
Experimental results demonstrated that all evaluated models can provide an effective and practical solution for intelligent
could identify and classify network traffic flows with network monitoring, contributing to the development of
satisfactory performance. Among the tested approaches, the lightweight cybersecurity systems capable of operating
RF classifier achieved the best overall performance, reaching efficiently in modern distributed networking environments.
a classification accuracy of 98.46% and a weighted F1-score
exceeding 0.98. The TensorFlow Lite implementation
REFERENCES
achieved an accuracy of 90.98%, demonstrating that efficient [1] S. Kumari, V. Tulshyan, and H. Tewari, “Cyber Security on the Edge:
Efficient Enabling of Machine Learning on IoT Devices,” Information
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on October 16,2026 at 16:36:48 UTC from IEEE Xplore. Restrictions apply.

2024, Vol. 15, Page 126, vol. 15, no. 3, p. 126, Feb. 2024, doi: [14] R. T. Elmaghraby, N. M. Abdel Aziem, M. A. Sobh, and A. M. Bahaa-
10.3390/INFO15030126. Eldin, “Encrypted network traffic classification based on machine
[2] H. G. A. Umar et al., “Energy-efficient deep learning-based intrusion learning,” Ain Shams Engineering Journal, vol. 15, no. 2, p. 102361,
detection system for edge computing: a novel DNN-KDQ model,” Feb. 2024, doi: 10.1016/J.ASEJ.2023.102361.
Journal of Cloud Computing 2025 14:1, vol. 14, no. 1, pp. 32-, Jul. [15] S. Sattar et al., “Anomaly detection in encrypted network traffic using
2025, doi: 10.1186/S13677-025-00762-9. self-supervised learning,” Scientific Reports 2025 15:1, vol. 15, no. 1,
[3] J. Li, B. Feng, and H. Zheng, “A survey on VPN: Taxonomy, roles, pp. 26585-, Jul. 2025, doi: 10.1038/s41598-025-08568-0.
trends and future directions,” Computer Networks, vol. 257, Feb. 2025, [16] R. W. K. S. Wijethilaka, K. Yapa, and D. Siriwardena, “A cost effective
doi: 10.1016/j.comnet.2024.110964. machine learning based network intrusion detection system using
[4] J. Anyam, R. R. Singh, H. Larijani, and A. Philip, “Empirical Raspberry Pi for real time analysis,” PLoS One, vol. 20, no. 12, p.
Performance Analysis of WireGuard vs. OpenVPN in Cloud and e0331123, Dec. 2025, doi: 10.1371/JOURNAL.PONE.0331123.
Virtualised Environments Under Simulated Network Conditions,” [17] G. Wang and Y. Gu, “Multi-Task Scenario Encrypted Traffic
Computers 2025, Vol. 14, Page 326, vol. 14, no. 8, p. 326, Aug. 2025, Classification and Parameter Analysis,” Sensors 2024, Vol. 24, Page
doi: 10.3390/COMPUTERS14080326. 3078, vol. 24, no. 10, p. 3078, May 2024, doi: 10.3390/S24103078.
[5] T. T. Nguyen and V. J. Reddi, “Deep Reinforcement Learning for [18] A. Skendzic and B. Kovacic, “Open source system OpenVPN in a
Cyber Security,” IEEE Trans. Neural Netw. Learn. Syst., vol. 34, no. function of Virtual Private Network,” IOP Conf. Ser. Mater. Sci. Eng.,
8, pp. 3779–3795, Nov. 2021, doi: 10.1109/TNNLS.2021.3121870. vol. 200, no. 1, p. 012065, May 2017, doi: 10.1088/1757-
[6] S. Rezaei and X. Liu, “Deep Learning for Encrypted Traffic 899X/200/1/012065.
Classification: An Overview,” IEEE Communications Magazine, vol. [19] S. G. Hussein and S. M. F. U. Rehman, “Protocol Efficiency and
57, no. 5, pp. 76–81, May 2019, doi: 10.1109/MCOM.2019.1800819. Resource Utilization in VPN Technologies: A Comparative Analysis
[7] M. A. Ferrag, L. Maglaras, S. Moschoyiannis, and H. Janicke, “Deep of OpenVPN and WireGuard,” Journal of Techniques, vol. 7, no. 4, pp.
learning for cyber security intrusion detection: Approaches, datasets, 37–42, Dec. 2025, doi: 10.51173/JT.V7I4.2768.
and comparative study,” Journal of Information Security and [20] Z. Sun, G. Wang, P. Li, H. Wang, M. Zhang, and X. Liang, “An
Applications, vol. 50, p. 102419, Feb. 2020, doi: improved random forest based on the classification accuracy and
10.1016/J.JISA.2019.102419. correlation measurement of decision trees,” Expert Syst. Appl., vol.
[8] M. Lopez-Martin, B. Carro, A. Sanchez-Esguevillas, and J. Lloret, 237, p. 121549, Mar. 2024, doi: 10.1016/J.ESWA.2023.121549.
“Network Traffic Classifier with Convolutional and Recurrent Neural [21] R. Yuan, Z. Li, X. Guan, and L. Xu, “An SVM-based machine learning
Networks for Internet of Things,” IEEE Access, vol. 5, pp. 18042– method for accurate internet traffic classification,” Information
18050, Sep. 2017, doi: 10.1109/ACCESS.2017.2747560. Systems Frontiers 2008 12:2, vol. 12, no. 2, pp. 149–156, Jul. 2008,
[9] M. C. Belavagi and B. Muniyal, “Performance Evaluation of doi: 10.1007/S10796-008-9131-2.
Supervised Machine Learning Algorithms for Intrusion Detection,” [22] A. Hirsi et al., “HSF: A Hybrid SVM-RF Machine Learning
Procedia Comput. Sci., vol. 89, pp. 117–123, Jan. 2016, doi: Framework for Dual-Plane DDoS Detection and Mitigation in
10.1016/J.PROCS.2016.06.016. Software-Defined Networks,” IEEE Access, vol. 13, pp. 112303–
[10] S.-A. Drăgușin, R.-N. Boştinaru, N. Bizon, and G.-V. Iana, “AI-Based 112323, 2025, doi: 10.1109/ACCESS.2025.3583712.
Embedded Framework for Cyber-Attack Detection Through Signal [23] S. E. Adi and A. J. Casson, “Design and optimization of a TensorFlow
Processing and Anomaly Analysis,” Applied Sciences 2026, Vol. 16, Lite deep learning neural network for human activity recognition on a
Page 1416, vol. 16, no. 3, p. 1416, Jan. 2026, doi: smartphone,” Proceedings of the Annual International Conference of
10.3390/APP16031416. the IEEE Engineering in Medicine and Biology Society, EMBS, vol.
[11] W. Shi, J. Cao, Q. Zhang, Y. Li, and L. Xu, “Edge Computing: Vision 2021-January, pp. 7028–7031, 2021, doi:
and Challenges,” IEEE Internet Things J., vol. 3, no. 5, pp. 637–646, 10.1109/EMBC46164.2021.9629549.
Oct. 2016, doi: 10.1109/JIOT.2016.2579198. [24] R. P. Ltd, “Raspberry Pi Compute Module 5,” 2022.
[12] D. Norris, “Machine Learning with the Raspberry Pi: Experiments with [25] “IP Network Traffic Flows Labeled with 75 Apps.” Accessed: May
Data and Computer Vision,” Machine Learning with the Raspberry Pi: 31, 2026. [Online]. Available:
Experiments with Data and Computer Vision, pp. 1–568, Jan. 2019, https://www.kaggle.com/datasets/jsrojas/ip-network-traffic-flows-
doi: 10.1007/978-1-4842-5174-4. labeled-with-87-apps/data
[13] Y. S. Razooqi and A. Pekar, “Binary VPN Traffic Detection Using [26] R. N. Boştinaru, S. A. Drǎguşin, N. Bizon, D. Cazacu, and G. V. Iana,
Wavelet Features and Machine Learning,” 2025 33rd International “Fire Detection Using Sound Analysis Based on a Hybrid Artificial
Conference on Software, Telecommunications and Computer Intelligence Algorithm,” Algorithms 2026, Vol. 19, Page 240, vol. 19,
Networks, SoftCOM 2025, Feb. 2025, doi: no. 3, p. 240, Mar. 2026, doi: 10.3390/A19030240.
10.23919/softcom66362.2025.11197436.
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on October 16,2026 at 16:36:48 UTC from IEEE Xplore. Restrictions apply.