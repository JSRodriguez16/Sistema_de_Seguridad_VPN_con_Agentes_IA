Proceedings of the Third International Conference on Innovations in Cybersecurity and Data Science (ICICDS-2026)
IEEE Xplore Part Number: CFP261CP-ART; ISBN: 979-8-3195-3130-8
Real Time VPN Traffic Attack Detection and
Classification
N. Chidambaresh S Charukkesh Dhivya G
Dept. of Electronics & Comm. Dept. of Electronics & Comm. Dept. of Electronics & Comm.
SRM Institute of Science & Technology SRM Institute of Science & Technology SRM Institute of Science & Technology
Chennai, India Chennai, India Chennai, India
cn7414@srmist.edu.in cs1838@srmist.edu.in dg0056@srmist.edu.in
VN Arumbu
Dept. of Electronics & Comm.
SRM Institute of Science & Technology
Chennai, India
arumbuv1@srmist.edu.in
Abstract—Virtual Private Networks (VPN) are used by many Network (VPN) the entire search process is secure & encrypted.
legitimate users all over the globe as it ensures data confidentiality VPN server acts as a medium to tunnel the data that is searched
over public networks. With the improvement in the current
and the website interacts with the VPN server instead of actual
technologies the chances of misusing data over transmission is
ISP. The ISP can now witness only the individual’s
prevalent. The way in which VPN ensures confidentiality may
however turn as a advantage for the data manipulators to indulge connectivity with the VPN server and not the actual data or
in fraudulent activities. VPN provides protection against Internet search made by the individual. VPN is a technology that will
Service Providers (ISP) to avoid tracking user activities and it may create a secure and effective tunnel between the user and
provide undesirable benefit to manipulators by exploiting
the internet. This VPN server provides the benefit of Privacy to
encrypted traffic patterns and thereby simulating cyber attacks.
hide the IP address, location, also to encrypt and protect the
Therefore, to ensure the use of VPN only for legitimate users
and to detect malicious activities of hackers in the presence of VPN data from attackers when using public network. However,
requires a system that differentiates the suspicious and normal attackers tend to misuse VPN for their own advantage, as the
activity. This problem is addressed through our idea by designing hackers use VPN server to hack other systems there are no
a system to detect and classify the malicious activity (Port Scan or
possibility of using existing systems like Firewall, Intrusion
not) in the presence of VPN. The system employs a real time VPN
Detection System, etc to block their activities.
attack simulation environment (Port Scan), Detection and
Classification of Port Scan using Machine Learning Techniques.
This creates an added advantage for the intruders to execute
Port Scan is a network reconnaissance technique to probe target
various manipulation activities, hiding their IP address and
host to detect the open, closed and filtered ports. This port scan
attack is detected and the system classifies if the attack is port scan safeguarding their origin. They may also switch VPN servers
or not. The real time VPN environment is setup in Linux to or accounts that increases the chance of becoming untraceable.
simulate normal, malicious traffic and Machine Learning This can adversely affect the VPN servers used by legitimate
Techniques are trained using a dataset to detect the malicious
users. The security systems may block legal VPN users or their
traffic and classify if its a port scan attack or not. Integrating the
VPN traffic maybe treated as suspicious.
designed ML model on to a real time VPN environment will
monitor the traffic network using pcap file and detect the presence
There are various attacks initiated by the Cyber criminals
of attack and classify the environment as port scan induced attack
including DDoS Attacks, Phishing activities, Botnet command,
environment or not. This system thereby understands the VPN
environment, the Port Scan attack and enhance VPN security for Credential stuffing & Brute force Attack, etc. Some other
legitimate users. threats include Vulnerability in VPN protocols, Misclassifi-
cation of VPN traffic as intruders may disguise themselves
Index Terms—Virtual Private Network, Legitimate users,
Cyberattacks, Port scan, Machine Learning Techniques. as legitimate traffic. They may exfiltrate senstive corporate
datas via enterprise VPN or use Malware over VPN by
delivering malware payloads through the VPN tunnel to make
I. INTRODUCTION
the detection process harder. This creates a need to handle
The advent rise of the technologies over the days has the intruders and protect legitimate users from any attacks
drastically improved the internet’s connectivity. The massive in the presence of VPN. Employing deep learning techniques
growth in today’s prominent fields is due to faster internet including autoencoders, CNNs, RNNs, DBNs can be effective
accessibility. The request to open any website or app via for intrusion detection [1], further Encrypted traffic
internet is monitored by the ISP which witnesses the websites classification performed using Deep Learning outperformed
an individual has visited. However, while using Virtual Private Shallow Machine Learning approaches for mobile human
data traffic [2],
979-8-3195-3130-8/26/$31.00 ©2026 IEEE 1375
79940611.6202.62507SDCICI/9011.01
:IOD
|
EEEI
6202©
00.13$/62/8-0313-5913-8-979
|
)SDCICI(
ecneicS
ataD
dna
ytirucesrebyC
ni
snoitavonnI
no
ecnerefnoC
lanoitanretnI
drihT
6202
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on October 16,2026 at 16:35:19 UTC from IEEE Xplore. Restrictions apply.

Proceedings of the Third International Conference on Innovations in Cybersecurity and Data Science (ICICDS-2026)
IEEE Xplore Part Number: CFP261CP-ART; ISBN: 979-8-3195-3130-8
likewise Deep Packet approach is utilized for application acts as the classifier model which is compared and evaluated
identification and Encrypted traffic characterization [3]. A against the model built with the Shallow Machine learning, to
Network Intrusion Detection system for traffic classification is conclude that Deep Learning outperforms the latter Machine
also developed through Deep learning for tackling challenges Learning technique also highlighting the risks against biased
such as high computational overhead, imbalanced class inputs [2]. Encrypted traffic data can further be classified using
distribution and the limitations of outdated datasets [4]. The Deep packet approach to achieve 98% of application
existing VPN IDS focus on encrypted traffic classification, identification and 94% of traffic characterization accuracy [3].
employing static dataset and building models with high In the same way an Intrusion Detection System primarily
computational requirements, our work focuses on simulating employing deep learning is built to address the issues including
attacks within a VPN environment to derive conclusions on class imbalance, lack of real world validation and outdated
attack presence and classification employing a Linux based datasets [4]. Statistical techniques for encrypted traffic data
Framework, thereby monitoring the attacks and analyzing its classification were studied and its metrics were evaluated
pattern for further security enhancements. As the VPN protects [5]. Network Anomalies are identified through various ML
the data, the detection of malicious activities pose difficulty, for algorithms namely Neural networks, Support Vector Machines,
which alternatively the packet sizes are studied, timing and Random Forest for improving network security [6]. Traffic
patterns are understood to analyze the packet. Classification identification through ML approaches improve the overall
algorithms are developed with Machine learning models to network security and efficiency [7]. Various ML models are
detect and identify abnormal VPN traffic, unusual traffic spikes built to analyse the traffic anomalies [8]. This Traffic detection
and port usage. and analysis process might improve the overall mitigation
strategies to overcome other attacks categories [9]. The
A linux Based malicious detection and classification system
abnormality in traffic patterns are studied to understand the
capable of identifying whether the traffic is of the attackers
attacker behaviour in high volume networks [10]. Network
or legitimate users is designed, additionally the system labels
traffic is handled through various techniques, its classification
whether the attack generated is Port Scan or not. The system
results are derived by employing Active learning [11] which
tends to classify the detected activity as Port Scan or benign to
proves to be a efficient traffic classification methodology by
derive effective countermeasures for the generated Port Scan
reducing the requirements of labeled data. In addition, Machine
attack. The system intends to understand traffic patterns in the
Learning can be applied to detect and classify various attacks
presence of VPN and rapidly monitors the activity, thereby
like Malware, DDoS, Phishing etc. using supervised,
classifying the environment is intruded or not. This system
unsupervised, ensemble and deep learning trends [12]. The Man
classifies the attack features, paving the way for the
in The Middle attack (MITM) is studied and simulated to
development of a required solution to avoid it. This framework
understand its behaviour, there are various solutions to handle
can be expanded for other types of attacks by simulating them
the problems of MITM attacks as discussed [13]. Specific
within a VPN server and evaluating the system performance to
attack categories and widely recognized attack types like DDoS
improve the accuracy. This provides an effective solution to
and Botnet are further understood by employing ML algorithms
avoid the misuse of VPN servers in various enterprises, thereby
and mitigated using traditional techniques, in which ML based
upholding the privacy of legitimate users.
techniques holds higher success rate compared to other
methods [14] [17]. DDoS attack detection and prediction can
II. LITERATURE SURVEY
be performed using ML algorithms by analyzing the SDN
Virtual Private Networks (VPN) provide secure tunnel to network for the feature collection process [15] and building
handle private documents and data by avoiding ISP’s detection. Intrusion Detection System to detect and analyse DDoS attacks
This creates an added advantage for attackers to indulge in [16]. Botnet attacks are detected and mitigated using Machine
malicious activities and it might lead to misinterpretation of Learning Algorithms for efficient network conditions [18] [19].
legitimate users as intruders. This creates a requirement of In most of the real time scenarios, attack detection and
generating solutions to detect the attack, classify it and analyze prediction becomes crucial and this can be achieved by
the same for initiating appropriate countermeasures. As integrating ML algorithms in real time conditions after training
traditional methods like Signature IDS cannot detect unknown the Model with appropriate dataset to reflect the detection of
attacks, there is a requirement of manually updating the rules. attackers [20]. However, in the presence of VPN attackers tend
To produce high false positives, ML algorithms can be utilized to use the network for hacking, data stealing etc, that creates
in which the traffic patterns are studied and the attacks are difficulty in understanding their activity under VPN tunnel.
accurately analyzed with continuous training of the model. There are various cross-protocol attacks that increase the
Intrusion Detection systems are developed to effectively work vulnerability in the network and protocol based (IPsec) under
against attacks and these systems employ deep learning the VPN Gateway [21]. This is mitigated through specific
techniques including autoencoders, CNNs, RNNs, DBNs and tunneling techniques and protocol selection for VPN which are
evaluates metrics by identifying key challenges like poor studied to understand their strengths and weaknesses [22].
detection and outdated datasets [1]. Encrypted mobile traffic
data is studied and classified using various approaches, Deep ML based IDs approaches are exhaustively studied for
learning.
979-8-3195-3130-8/26/$31.00 ©2026 IEEE 1376
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on October 16,2026 at 16:35:19 UTC from IEEE Xplore. Restrictions apply.

Proceedings of the Third International Conference on Innovations in Cybersecurity and Data Science (ICICDS-2026)
IEEE Xplore Part Number: CFP261CP-ART; ISBN: 979-8-3195-3130-8

encrypted, anomalous traffic, for specific attack categories and
| VPN  specific  |     | vulnerabilities.  |     | However,  |     | very  few  | works  |     |     |     |     |
| -------------- | --- | ----------------- | --- | --------- | --- | ---------- | ------ | --- | --- | --- | --- |
combine the two: validating an ML-based detector on traffic
captured live, inside an active VPN tunnel, rather than on
an offline dataset. The proposed system uses a controlled
| deployment  | that  | validates  |     | performance  | directly  |     | in  a  live  |     |     |     |     |
| ----------- | ----- | ---------- | --- | ------------ | --------- | --- | ------------ | --- | --- | --- | --- |
VPN tunneling environment, while still employing the offline
dataset for a large and diverse training base.
| The  primary  |     | contribution  |     | of  | this  work  | includes  | the  |     |     |     |     |
| ------------- | --- | ------------- | --- | --- | ----------- | --------- | ---- | --- | --- | --- | --- |
development of controlled, repeatable real-time VPN attack
simulation environment built on WireGuard and the extraction
of the flow based statistical features from the encrypted VPN
traffic environment using CICFlowmeter. A two stage ML
| detection  | &   | classification  |     | framework  | is  | developed  | and  |     |     |     |     |
| ---------- | --- | --------------- | --- | ---------- | --- | ---------- | ---- | --- | --- | --- | --- |
validated in real-time with the live attack situations.
III.  SYSTEM DESCRIPTION
The Real Time VPN Attack Detection and Classification
system is intended to normalise Virtual Private Network usage
for legitimate users. Developing a system for this safe and
secure form of VPN usage provides integrity and enhancement
| of  legal   | user’s       | activities.  |            | The  system  | integrates  |         | various  |     |     |     |     |
| ----------- | ------------ | ------------ | ---------- | ------------ | ----------- | ------- | -------- | --- | --- | --- | --- |
| individual  | sub-systems  |              | including  |              | Attacker,   | Victim  | and      |     |     |     |     |
Analyser, which replicates a real time model of an Intrusion
Detection System that will understand the attack simulated,
detect its origin and even signify whether this environment is a
malicious or normal traffic. This is achieved by training the
| Machine  | Learning  | model  |     | with  | continuous  | and  | updated  |     |     |     |     |
| -------- | --------- | ------ | --- | ----- | ----------- | ---- | -------- | --- | --- | --- | --- |
datasets. The system model, its working, steps of operation,
| execution  | and  | the  | Machine  | Learning  |     | classification  | are  |     |     |     |     |
| ---------- | ---- | ---- | -------- | --------- | --- | --------------- | ---- | --- | --- | --- | --- |
discussed briefly.

A. Overview of the system
attacks
| The  implemented  |     |     | system  | is  optimised  |     | to  detect  |     |     |     |     |     |
| ----------------- | --- | --- | ------- | -------------- | --- | ----------- | --- | --- | --- | --- | --- |
Fig. 1.  Block Diagram of the System
and classify the Port Scan attack environment compared to a

normal environment within a VPN setup. There are various
operational steps and mechanisms upon which the system

works as depicted in Fig. 1. The Attack Generation layer is
employs dedicated /24 subnets for endpoints, a UDP listening
| where the VPN tunnel is being set up and generation of  |     |     |     |     |     |     | Port  |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
port (51820) and default WireGuard handshake interval. The
| Scan  attack  | takes place.  |     | Data  | Capture  | and  | Analysis  | layer  |                  |             |                           |          |
| ------------- | ------------- | --- | ----- | -------- | ---- | --------- | ------ | ---------------- | ----------- | ------------------------- | -------- |
|               |               |     |       |          |      |           |        | VPN  decryption  | and packet  | capture  is  carried out  | on  the  |
captures the network packets and then analyses it to extract
interface producing the outer-tunnel PCAP, while the inner
flow based statistical features. This layer includes the victim
traffic destined for Victim VM addressed in the 10.20.20.x
system that experiences the attack and the analyser system that
range is forwarded using IP routing.
analyses the attack patterns. The ML Layer is responsible for
| identification and classification of the malicious VPN traffic  |     |     |     |     |     |     |     |     |     |     |     |
| --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
with the Random forest- XGboost framework developed.
The Victim VM runs an Apache HTTP server which ensures
B. WireGuard VPN setup and Network Topology
that the Analyser alone observes the encrypted traffic at the
The  Fig.  1  describes  that  our  system  setup  consists  of  point of capture, producing the conditions of a real VPN
three  Virtual  Machines  connected  through  a  private  host- provider. For traffic generation, the Attacker uses NMAP  with
only network. The Attacker VM (Kali Linux) and Analyser VM  multiple  scan  profiles  including  -  TCP  SYN  scans,  TCP
(Ubuntu)  are  connected  through  a  WireGuard  tunnel: the  connect scans and service detection scans with different time
| Analyser  | exposes  | a   | wg0  | Wireguard  | interface,  |     | the  traffic  |     |     |     |     |
| --------- | -------- | --- | ---- | ---------- | ----------- | --- | ------------- | --- | --- | --- | --- |
templates. These are exposed to the Apache service to produce
generated by the attacker is encapsulated inside the WireGuard  Port Scan flows, however benign traffic is generated with
UDP  tunnel  before  connecting  with  the  Analyser.  The  normal HTTPS requests from the Attacker/Analyser side to
Wireguard,  being  a  lightweight  and  modern  cryptographic  both the Victim VM and to external internet hosts to maintain
design was  selected  to  serve  the  purpose  of  tunneling.  the dataset with a realistic assortment of internal and external
| Wireguard  |     |     |     |     |     |                                        |     | benign flows along with the Port Scan Flows.  |     |     |      |
| ---------- | --- | --- | --- | --- | --- | -------------------------------------- | --- | --------------------------------------------- | --- | --- | ---- |
|            |     |     |     |     |     | 979-8-3195-3130-8/26/$31.00 ©2026 IEEE |     |                                               |     |     | 1377 |
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on October 16,2026 at 16:35:19 UTC from IEEE Xplore.  Restrictions apply.

Proceedings of the Third International Conference on Innovations in Cybersecurity and Data Science (ICICDS-2026)
IEEE Xplore Part Number: CFP261CP-ART; ISBN: 979-8-3195-3130-8
| C. Dataflow Description  |     |     |     |     |     |     |     | IV. METHODOLOGY  |     |     |     |
| ------------------------ | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- |
The system function starts with the Wireguard VPN tunnel  The purpose of this system is to adopt advanced technologies
establishment  between  the  Attacker  and  analyser  system  to enhance the VPN tunneling process and provide legitimate
access to normal users. This system’s integration with various
| ensuring  | an  encrypted  | communication  |     | between  |     | both  the  |     |     |     |     |     |
| --------- | -------------- | -------------- | --- | -------- | --- | ---------- | --- | --- | --- | --- | --- |
systems. Once both the systems are connected through VPN  mitigation techniques avoid intruders entry in VPN  presence.
The system model works in a sequential way integrating the
tunnel, a Port Scan attack is generated from the attacker system
employed technologies and the complete system workflow is
in the presence of the VPN to mimic the real-time intrusion
| scenario. The victim system experiences the generated attack  |                                                |     |     |     |     |     | discussed.  |     |     |     |     |
| ------------------------------------------------------------- | ---------------------------------------------- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- |
| traffic and                                                   | analysed by the analyser system. The analyser  |     |     |     |     |     |             |     |     |     |     |
A. Preparation of Environment
system captures network packets by monitoring the traffic
packets transmitted through  the  VPN  tunnel.  The  captured  The work setup is depicted in Fig 2. starts with establishing
a virtualised Linux environment with three virtual machines
| packets  | are  stored  | as  PCAP  |     | files  and  | analysed  | using  |     |     |     |     |     |
| -------- | ------------ | --------- | --- | ----------- | --------- | ------ | --- | --- | --- | --- | --- |
CICFlowmeter  to  extract  numerical and statistical features  Attacker, Analyser and Victim systems. The attacker system is
including flow duration, byte rates, flag information, packet  deployed in the Kali linux with the Nmap, a tool for network
|         |                     |         |      |          |            |       | scanning. This Nmap is used for the generation of  |     |     | the  | Port  |
| ------- | ------------------- | ------- | ---- | -------- | ---------- | ----- | -------------------------------------------------- | --- | --- | ---- | ----- |
| counts  | and  inter-arrival  | times.  | The  | dataset  | extracted  | then  |                                                    |     |     |      |       |
undergoes  feature  preprocessing  stages  to  begin  the  ML  scan  traffic  over  the  network.  The  analyser  system  is
deployed as the central monitoring system in Ubuntu and
| classification.  | The  | developed  | Random  | forest  | -   | XGboost  |     |     |     |     |     |
| ---------------- | ---- | ---------- | ------- | ------- | --- | -------- | --- | --- | --- | --- | --- |
framework involves both the models, where the Random Forest  integrates with VPN tunnel established using Wireguard. The
model is employed for traffic identification, XGboost model  CIC flowmeter, Python are installed in the Analyser system.
|     |     |     |     |     |     |     | The  network  | packets  passing  | through  | the  VPN  tunnel  | is  |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ----------------- | -------- | ----------------- | --- |
determines whether the detected activity corresponds to a Port
Scan attack or benign traffic.  captured and monitored using tcpdump and Zeek, it is then used
for obtaining the packet traces for further processing. The

Victim system running in Ubuntu hosts a target web service
D. Dataset and Features
using Apache HTTP server to emulate a real time network
Machine  Learning  Techniques  are  employed  for  this  service that could be probed during the attack simulation.
detection and classification process, in which these techniques
| include                                                  | the  responsibility  |     | of  successful  | implementation  |     | of  |     |     |     |     |     |
| -------------------------------------------------------- | -------------------- | --- | --------------- | --------------- | --- | --- | --- | --- | --- | --- | --- |
| secure mechanism for legitimate VPN users. The ML model  |                      |     |                 |                 |     |     | is  |     |     |     |     |
trained with an existing dataset and feature extraction from
| the dataset helps in identifying the presence of attack  |     |     |     |     |     | and its  |     |     |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
type. CIC-IDS 2017 dataset is used for training and augmented
| with Newly captured VPN based traffic. Each Network  |     |     |     |     |     | flow  |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
consists of the following features such as Total Forward and
Backward Packets, Flow duration, Average Packet Length,
Number of unique destination ports, Packet rates (packets /
sec), Flag counts, Bytes per flow etc. After the data is combined
and augmented, the resulting dataset includes 956,961 benign
flow records, 11,086 malicious flow records to sum up a total
of 968,047 labeled flows. On preprocessing the dataset, 77
numerical flow features were extracted per record, the dataset
was split into 774,453 training flows and remaining were
reserved for validation and testing to preserve the (highly
imbalanced) class ratio. All these 77 numerical features were
retained and undefined values are assigned with the median of
| each  feature  | column.  | The  | most  | pivotal  | features  | for  |     |     |     |     |     |
| -------------- | -------- | ---- | ----- | -------- | --------- | ---- | --- | --- | --- | --- | --- |
differentiating the malicious and benign flows based on feature
|             |         |             |           |     |                |       |     | Fig. 2.  | Virtual Machine setup  |     |     |
| ----------- | ------- | ----------- | --------- | --- | -------------- | ----- | --- | -------- | ---------------------- | --- | --- |
| importance  | scores  | are:  flow  | duration  | &   | inter-arrival  | time  |     |          |                        |     |     |

statistics - that capture rapid probing behaviour of the attack,

packet-rate and bytes per second features - to analyse small
B. Defining Attack Scenarios
packets in quick succession, forward/backward packet length
At this point, controlled attack scenarios were set up to test
statistics to witness large and variable payloads of a genuine
flow, TCP Flag count features indicating the half-open and  the system in the VPN environment with malicious traffic. The
main attack that was simulated in this work is Port Scan.
| rejected  | connection  | attempts  | made  | by  SYN-scan.  |     | These  |     |     |     |     |     |
| --------- | ----------- | --------- | ----- | -------------- | --- | ------ | --- | --- | --- | --- | --- |
The attacker node used Nmap to look for services on the victim
features were helpful in differentiating the attack and benign
|     |     |     |     |     |     |     | machine.  | Port  Scan  attack  | was  selected  | for  the  following  |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------------------- | -------------- | -------------------- | --- |
traffic and are consistent with flow-level signatures for port
reasons, one being the common reconnaissance
scan traffic.
|     |     |     |     |     | 979-8-3195-3130-8/26/$31.00 ©2026 IEEE |     |     |     |     | 1378 |     |
| --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | ---- | --- |
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on October 16,2026 at 16:35:19 UTC from IEEE Xplore.  Restrictions apply.

Proceedings of the Third International Conference on Innovations in Cybersecurity and Data Science (ICICDS-2026)
IEEE Xplore Part Number: CFP261CP-ART; ISBN: 979-8-3195-3130-8
technique used by intruders before launching a more vital  byte counts and timestamps. These features are then used for
follow-up attack. Second, the attack produces a distinctive  training the ML model to detect and classify the malicious
| flow-level signature like short flows, high packet rates and flag  |     |           |                      |     |       | traffic.  |     |     |     |     |     |
| ------------------------------------------------------------------ | --- | --------- | -------------------- | --- | ----- | --------- | --- | --- | --- | --- | --- |
| patterns that remain well suited to validate whether flow-based,   |     |           |                      |     |       |           |     |     |     |     |     |
| payload-independent                                                |     | features  | are  discriminative  |     | once  | the       |     |     |     |     |     |
traffic is encrypted inside a VPN tunnel. Third, this attack
allows controlled testbed, run-manifest methodology that are
focused to understand the attack type and validated thoroughly
before extending to further attacks.
In addition to this attack, the CIC-IDS 2017 training data
includes FTP-Patator and SSH-Patator brute-force attack flows,
the XGBOOST stage is trained as a multi-classifier model even
though the paper focuses on a single attack category. The attack
| agnostic system produces the traffic and is tunneled, captured  |     |     |     |     |     |     |     |     |     |     |     |
| --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and converted to flow features. Additional attack types such as
|              |         |              |          |        |        |          |     | Fig. 4.  | Generated Pcap File  |     |     |
| ------------ | ------- | ------------ | -------- | ------ | ------ | -------- | --- | -------- | -------------------- | --- | --- |
| Distributed  | Denial  | of  Service  | (DDoS),  | brute  | force  | login    |     |          |                      |     |     |
attempts, botnet and malware propagation can be reproduced

through augmentation of Attacker’s traffic generation  tool  D. Feature Engineering and Dataset Preparation
| employing  | the  | WireGuard  | tunnel.  | A  run  | manifest  | is  |     |     |     |     |     |
| ---------- | ---- | ---------- | -------- | ------- | --------- | --- | --- | --- | --- | --- | --- |
The Random forest-XGboost framework was created using
maintained to ensure the experiments are repeated. It keeps
flow-based network traffic features extracted using the CIC-
track of the run identifier, attack type, start and end times for
IDS 2017 intrusion detection datasets and real-time captured
each experiment.
VPN traffic. Multiple CSV files containing benign traffic,

brute-force attacks and port scanning attacks were combined to
|     |     |     |     |     |     | form  a  | training  | dataset.  | During  preprocessing,  |     | non-feature  |
| --- | --- | --- | --- | --- | --- | -------- | --------- | --------- | ----------------------- | --- | ------------ |
identifier columns such as flow IDs, IP addresses, ports and
timestamps were removed to avoid data leakage and ensure that
|     |     |     |     |     |     | only  traffic  | attributes  | of  | behavioral  | patterns  | were  used to  |
| --- | --- | --- | --- | --- | --- | -------------- | ----------- | --- | ----------- | --------- | -------------- |
train the model. All other columns were encoded numerically.
|     |     |     |     |     |     | Incomplete  | and  | undefined  | values  were  | replaced  | using  a  |
| --- | --- | --- | --- | --- | --- | ----------- | ---- | ---------- | ------------- | --------- | --------- |
median-based imputation technique. The final dataset consists
of numerical flow features that include packet statistics, byte
counts, packet lengths, flow duration and traffic rate features.
A binary label was created to separate benign and malicious
traffic and attack classes were preserved to conduct a multi
category classification. The Final dataset is split (70/15/15 by
runs) in the following scale for training and testing using a
stratified sampling technique to avoid the leakage of data.

Fig. 3.  Simulated Port Scan Attack  E. Model Training and Optimization
|     |     |     |     |     |     | The Machine learning Framework is built as a two-step  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------------------------ | --- | --- | --- | --- | --- |
C. Generating Traffic and Extracting the flows
|     |     |     |     |     |     | classifying  | system.  | In  the  | initial  stage,  | a  binary  | intrusion  |
| --- | --- | --- | --- | --- | --- | ------------ | -------- | -------- | ---------------- | ---------- | ---------- |
Based on the defined experimental runs, network traffic was  detection model was developed to differentiate between benign
generated and monitored within the VPN environment. Fig 3.  traffic and malicious activity. This is accomplished using  a
depicts the simulated Port Scan attack. For each run listed  tree-based  ensemble  classifier  called  Random  Forest.  This
in the experiment manifest, packet capture is initiated at the  works well with high-dimensional tabular network traffic data.
Analyser system. The attacker then executes the corresponding  Fig. 5 best describes the model was trained with the balanced
Port Scan activity according to the scheduled timestamps in the  class  weights  to  reduce  the  effects  of  class  imbalance  in
manifest. The packet capturing is prolonged until the interval  intrusion  detection  datasets.  In  the  second  stage,  a  multi-
ends, after which the captured traffic is stored as the Packet  class classifier based on XGboost was used to classify the  type
Capture files (PCAP). One such generated PCAP file  is shown  of attack simulated. A label encoder was used to encode the
in  Fig  4.  These  PCAP  traces  are  further  processed  using  original attack labels, which were then used to train the model
CICFlowmeter to convert the packet level data into flow based  to differentiate the types of attacks in the dataset. Number of
records. The generated flow based data was exported as a CSV  estimators,  tree  depth  and  learning  rate  are  some
hyperparameters configured to enable effective learning of
| dataset  | containing  | key  network  | attributes  | like  | source  | &   |     |     |     |     |     |
| -------- | ----------- | ------------- | ----------- | ----- | ------- | --- | --- | --- | --- | --- | --- |
destination addresses, packet counts, port numbers, flags,  complex traffic patterns.
|     |     |     |     | 979-8-3195-3130-8/26/$31.00 ©2026 IEEE |     |     |     |     |     |     | 1379 |
| --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | --- | --- | ---- |
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on October 16,2026 at 16:35:19 UTC from IEEE Xplore.  Restrictions apply.

Proceedings of the Third International Conference on Innovations in Cybersecurity and Data Science (ICICDS-2026)
IEEE Xplore Part Number: CFP261CP-ART; ISBN: 979-8-3195-3130-8
prediction results summarized in Fig. 6 shows that flows directed
to the Internal host 10.0.2.3 were mostly classified as Port
Scan, while flows directed to external servers were identified as
benign. This signifies that the ML framework effectively
captures attack specific traffic patterns. The model achieved an
overall accuracy of 75%. For the Benign class, the obtained
precision is 1.00 and the recall rate of 0.67 was recorded, the
achieved F1 score of the model is 0.80. While for Port Scan
attack, a precision of 0.50, recall of 1.00 and F1-score of 0.67 is
achieved as depicted in Fig 7. The confusion matrix shows out
of 9 benign traffic flows, 6 were correctly identified as benign
and 3 were misclassified as Port Scan.
Fig. 5. Training Summary of the Model
F. Real-Time Evaluation and Analysis
Using a streaming loop that constantly takes in new flow
records, updates per-source buffers, applies the predefined
preprocessing steps and runs the trained classifiers for attack
detection, a real-time detection pipeline was added to the
analyzer system. Based on set thresholds, the system makes
predicted labels that show when malicious activity is
happening and keeps logs for each prediction. The Framework
is tested by sending live attacks from the attacker system at
Fig. 6. Live Detection and Classification Results
different levels of intensity and the network traffic was
monitored. Performance metrics such as detection accuracy,
per-attack evaluation measures, detection latency and
throughput were kept in track. The results were put into
organized tables, graphs and the failure rate was figured out
by analyzing the wrong predictions. The extracted traffic
characteristics and observed attack patterns also help in
making better datasets and would make it possible to use
signature-based intrusion detection and mitigation systems.
V. RESULTS AND DISCUSSION
The trained Machine learning framework is evaluated with
generated VPN flow data to assess its ability to differentiate
between benign traffic and malicious Port Scan attack. The
model was evaluated with augmented and live VPN streams,
on which the augmented dataset with a precision and recall
of 1.00 for benign class and 1.00/0.99 for malicious class
and the Downstream XGBoost classifier applied on the flows
already flagged as malicious, achieved an overall test accuracy
of 99.996%. This correctly distinguished the Port Scan, FTP-
Patator and SSH-Patator flows with precision, recall and F1-
Fig. 7. Confusion Matrix
score of 1.00 across all three classes as in Fig. 5. The results
show that for a large augmented dataset the flow level features
The augmented dataset based ML classification and real time
are highly separable for both benign/malicious class.
classification shows significant difference. These results show a
The trained ML framework was evaluated on flows recall-based trade-off, however every Port Scan flow in live
captured from live WireGuard testbed to assess its ability. The stream were correctly flagged at the cost of three benign flows
being misclassified as malicious. It is evident that the model
detects attack traffic with high recall though some false positives
remain. This trade-off is acceptable in security applications,
where detecting all the potential attacks is much prioritized and
can be improved further through feature refinement and model
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on October 16,2026 at 16:35:19 UTC from IEEE Xplore. Restrictions apply.
979-8-3195-3130-8/26/$31.00 ©2026 IEEE 1380

Proceedings of the Third International Conference on Innovations in Cybersecurity and Data Science (ICICDS-2026)
IEEE Xplore Part Number: CFP261CP-ART; ISBN: 979-8-3195-3130-8
tuning. [6] Deepika, D., Deepika Pogiri, Lokesh Raj Pandravisham, Yashwanth
Kumar Prudvi, and Sathvik Reddy Ramannagari. ”Anomaly network
traffic detection of wireless network system.” In 2024 5th International
VI. CONCLUSION
Conference on Electronics and Sustainable Communication Systems
(ICESC), pp. 703-708. IEEE, 2024.
The Real time VPN attack detection and classification system is [7] Rekha, DS BNS, VSSP Raju Gottumukkala, Gudapati Diana Kamal, and
designed and implemented as a secure encrypted network Shalini Eda. ”Enhancing network security: Ml-based anomaly detec-tion.”
In 2024 First International Conference for Women in Computing
communication. This system creates a controlled VPN
(InCoWoCo), pp. 1-5. IEEE, 2024.
environment between Attacker and Analyser, the system [8] Singh, Richa, Nidhi Srivastava, and Ashwani Kumar. ”Machine learning
successfully simulated the Port Scan attack. The Analyser captures techniques for anomaly detection in network traffic.” In 2021 sixth
and processes the VPN traffic, extracting the flow level features international conference on image information processing (ICIIP), vol. 6,
pp. 261-266. IEEE, 2021.
which in turn are analysed through Machine Learning models
[9] Agarwal, Sanchi, Ayon Somaddar, Paritosh Harit, Divya Thakur, Akshita
including Random Forest Classifier and XGBoost which detects Sharma, and Krishna Kaushal Singh. ”Network traffic analysis and
and classifies if there is an attack or not. The system achieved anomaly detection.” In 2023 3rd International Conference on Smart Gen-
eration Computing, Communication and Networking (SMART GEN-
reliable results by demonstrating that payload-independent, flow
CON), pp. 1-6. IEEE, 2023.
based features are effective for detecting Port Scan activity within [10] Elsayed, Mahmoud Said, Nhien-An Le-Khac, Soumyabrata Dev, and
VPN. While the offline Random Forest and XGBoost models Anca Delia Jurcut. ”Detecting abnormal traffic in large-scale networks.”
achieve near-perfect accuracy on large augmented dataset, the live In 2020 international symposium on networks, computers and commu-
nications (ISNCC), pp. 1-7. IEEE, 2020.
stream evaluation achieves 75% accuracy with perfect recall on
[11] Shahraki, Amin, Mahmoud Abbasi, Amir Taherkordi, and Anca Delia
Port Scan class. The principal limitations of the work include small Jurcut. ”Active learning for network traffic classification: A technical
live stream evaluation set limiting the live metrics statistically, study.” IEEE Transactions on Cognitive Communications and Network-
ing 8, no. 1 (2021): 422-439.
only a single attack was exercised although offline models support
[12] Cˇ atloch, Dusˇan, Eva Chovancova´, Martin Chovanec, and Martin Sˇtancel.
FTP-Patator and SSH-Patator classification, the current pipeline ”Application of Machine Learning Algorithms for Cybersecurity: De-
classifies flow independently that reduces false positives. Wire- tection and Classification of Malware, DDoS, and Phishing Attacks.”
Guard testbed is a controlled virtual environment and has not been In 2025 IEEE 29th International Conference on Intelligent Engineering
Systems (INES), pp. 000353-000358. IEEE, 2025.
valid on a production scale VPN traffic volume. The future work
[13] Ajuluchukwu, Melvin, Hayden Wimmer, and Atef Mohamed. ”Simulat-
focuses on expanding the live-capture for longer durations and ing Man-in-the-Middle Attacks: Techniques, Detection, and Mitigation
multiple attack scenarios to obtain robust live-stream metrics, Strategies.” In 2025 6th International Conference on Artificial Intelli-
gence, Robotics and Control (AIRC), pp. 447-451. IEEE, 2025.
Extension of attack generation layer to additional attack scenarios
[14] Pranav, S. A., and B. HariHaran. ”DDoS and botnet attacks: a survey of
such as DDoS, brute force logic, botnet command and malware detection and prevention techniques.” In 2024 International Conference
propagation thereby developing an agnostic design for attack on Advances in Data Engineering and Intelligent Computing Systems
detection and classification, Incorporating temporal features like (ADICS), pp. 1-7. IEEE, 2024.
per-source sliding window aggregation to reduce false positives
and explores deep learning sequence as an alternative to tree based
ensemble. We intend to emphasize an automated Cybersecurity
system that is capable of identifying attack behaviors constantly
and help in deriving more solutions to tackle these intrusions in a
VPN environment. This proposed approach contributes towards an
intelligent, privacy preserving Cybersecurity system and can
further be expanded as multi-class attack detection system with
improvements in detection accuracy using Deep Learning
algorithms.
REFERENCES
[1] Lansky, Jan, Saqib Ali, Mokhtar Mohammadi, Mohammed
Kamal Majeed, Sarkhel H. Taher Karim, Shima Rashidi,
Mehdi Hosseinzadeh, and Amir Masoud Rahmani. ”Deep
learning-based intrusion detection systems: a systematic
review.” IEEE access 9 (2021): 101574-101599.
[2] Aceto, Giuseppe, Domenico Ciuonzo, Antonio Montieri,
and Antonio Pescape´. ”Mobile encrypted traffic
classification using deep learning: Experimental
evaluation, lessons learned, and challenges.” IEEE trans-
actions on network and service management 16, no. 2
(2019): 445-458.
[3] Lotfollahi, Mohammad, Mahdi Jafari Siavoshani, Ramin
Shirali Hossein Zade, and Mohammdsadegh Saberian.
”Deep packet: A novel approach for encrypted traffic
classification using deep learning.” Soft Computing 24,
no. 3 (2020): 1999-2012.
[4] Ahmad, Zeeshan, Adnan Shahid Khan, Cheah Wai Shiang,
Johari Abdullah, and Farhan Ahmad. ”Network intrusion
detection system: A systematic study of machine learning
and deep learning approaches.” Transactions on Emerging
Telecommunications Technologies 32, no. 1 (2021):
e4150.
[5] Mahdavi, Ehsan, Ali Fanian, and Homa Hassannejad.
”Encrypted traffic classification using statistical features.”
(2018): 29-43
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on October 16,2026 at 16:35:19 UTC from IEEE Xplore. Restrictions apply.
979-8-3195-3130-8/26/$31.00 ©2026 IEEE 1381

Proceedings of the Third International Conference on Innovations in Cybersecurity and Data Science (ICICDS-2026)
IEEE Xplore Part Number: CFP261CP-ART; ISBN: 979-8-3195-3130-8
[15] Vijay, S., Nilamadhab Mishra, and Maistry Mohammed Ateeq. ”DDoS
Attack Detection and Prediction Using Machine Learning With Analysis
of SDN Network.” In 2025 International Conference on Advancements
in Smart, Secure and Intelligent Computing (ASSIC), pp. 1-5. IEEE,
2025.
[16] Fadhlillah, Aghnia, Nyoman Karna, and Arif Irawan. ”IDS performance
analysis using anomaly-based detection method for DOS attack.” In 2020
IEEE International Conference on Internet of Things and Intelligence
System (IoTaIS), pp. 18-22. IEEE, 2021.
[17] Thota, Swapna, and D. Menaka. ”Importance of machine learning algo-
rithms to detect botnet ddos attacks.” In 2022 International Conference
on Augmented Intelligence and Sustainable Systems (ICAISS), pp. 900-
903. IEEE, 2022.
[18] Alghamdi, Abdullah, and Ayad Barsoum. ”A comprehensive ids to detect
botnet attacks using machine learning techniques.” In 2024 IEEE 3rd
International Conference on Computing and Machine Intelligence
(ICMI), pp. 1-6. IEEE, 2024.
[19] Ramesh, R. Barath, and S. John Justin Thangaraj. ”Analyzing and detect-
ing botnet attacks using anomaly detection with machine learning.” In
2023 5th International Conference on Inventive Research in Computing
Applications (ICIRCA), pp. 911-915. IEEE, 2023.
[20] Sutar, Snehal, Piyusha Khune, Hrittika Gandhi, Kumari Snehal Patteba-
hadur, and Chetan N. Aher. ”Real time network attack detection using
machine learning techniques.” In 2023 14th International Conference on
Computing Communication and Networking Technologies (ICCCNT),
pp. 1-6. IEEE, 2023.
[21] Amaldeep, S., and Sriram Sankaran. ”Cross protocol attack on IPSec-
based VPN.” In 2023 11th International Symposium on Digital Forensics
and Security (ISDFS), pp. 1-6. IEEE, 2023.
[22] Jahan, Sohely, Md Saifur Rahman, and Sajeeb Saha. ”Application
specific tunneling protocol selection for Virtual Private Networks.” In
2017 international conference on networking, systems and security
(nsyss), pp. 39-44. IEEE, 2017.
979-8-3195-3130-8/26/$31.00 ©2026 IEEE 1382
Authorized licensed use limited to: Univ Distrital Francisco Jose de Caldas. Downloaded on October 16,2026 at 16:35:19 UTC from IEEE Xplore. Restrictions apply.