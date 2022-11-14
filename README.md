# EOCs

EsseCS Project Proposal

Group 35


1  The link layer in practice 

2 Project Description
The aim of this project is to gain (additional) knowledge of the link layer by simulating specific elements of the link layer. In doing so we will also show our knowledge of the link layer (a more detailed explanation is written in paragraph 6: The integration of  learning goals ). By making a network simulation and a data center network simulation in ns-3 and GNS3, respectively, we will show how the link layer works. In doing so, we will gain knowledge of the link layer and its intricacies. Secondly, we will use Python to make our own simulation for error detection and correction code with text files. A more in depth description for this part of the project is given further in the project description.

The simulation of the data center network we will create during this project will consist of a network simulation built in GNS3. We will first gather knowledge on the characteristics and possibilities of a LAN and data center networks, make possible routing tables and research how to use GNS3. This will be done for different data center types and topologies. In order for the devices in our network to communicate with each other, we will use routing tables. These tables will make sure that data will only be transmitted to the intended receiver, without creating unnecessary traffic in our network. After that we will set up our own virtual networks, which will reflect a data center network. Finally we will document all of our work to give a concise description and explanation on the discoveries we have made.

The second part of this project is to create a Python program, which will take a text file as input. The file will then be converted to bits, and an error will be put in either manually or with a randomiser. This simulates an error that could occur if we would have sent it through a real “network” with interference and other changes in voltages in the cables. Then a second program, or rather programs will check for the errors. All these programs will use a different kind of error detection and/or correction code, namely parity, crc, checksum and hamming distance.
Parity check:
In this code we will use parity checking to check if there is an error by adding a parity bit to the end of the bit string. This is merely an error detection method not a correction method. Furthermore, this method will only be successful if the number of errors in the string of bits is odd. Secondly we can use a matrix parity check, also known as a 2D parity check. This will also, or at least in most cases, tell where the error has occurred in the string of bits. 
CRC (Cyclic Redundancy Check)
CRC stands for Cyclic Redundancy Check. For the first part, it uses a long division. The remainder from the division is the checksum. If the remainder is not equal to 0 then the receiver knows that an error has occurred, otherwise the data is accepted as being correct.  It is possible to reverse engineer the divider to see where the error had occurred. 
Checksum						
The internet checksum is a checksumming method and a technique for detecting errors in which bytes of data are treated as 16-bit integers. The sum of all 16-bit integers is calculated. The 1’s complement of this sum is the internet checksum, which is added to the final sum total. The 1’s complement of the sum of the received data is then taken. If the result is all 0 bits, the data is validated. If there are any 1 bits, an error is indicated.
Hamming distance 
Hamming distance is defined as the number of bit positions in which two codewords differ. The number of bit positions in which two codewords differ is calculated by first performing a XOR operation, which will be performed bit by bit. Secondly, the result of the XOR operation will be summed and the result of that sum is the hamming distance.
If two code words are ‘d’ hamming distance apart, ‘d’ single bit errors are required to convert one into another. A block code is a code in which ‘r’ check bits are computed only as a function of ‘m’ data bits. A code with at least (d+1) distance is able to detect up to ‘d’ number of errors. A code with at least (2d+1) distance is able to correct up to ‘d’ number of errors.

3 Project Goal
The first goal of this project is to create network simulations of a data center for the purpose of storing and processing data. We will do this using GNS3, an open source network simulator, which is targeted primarily for research and educational use. We will do this for the different data center types and routing tables researched beforehand. 
The second goal is to create our own small scale error detection, and correction code. We want to achieve this in Python with the use of hamming and crc error-detections, and -correction methods with the goal of being able to input any type of text(file), flipping some bits at random to simulate the errors occurring, and correcting those errors using these methods.

4 Milestone

We have determined the following milestones:
Research on the characteristics and possibilities of GNS3 as a tool to set up a data center simulation and on ns-3 as a tool to set up a network simulation is completed. 
Multiple data centers on paper complete with LANs and routing tables.
A simulation of a small Local Area Network in ns-3.
Make the Python code for converting text files to usable bit strings for the error correction code.
Do all the research for each of the different detection and correction coding methods.
Set up basic outlines for each of the different detection and correction methods in Python.
Set up github.


5 Tasks

Name
Tasks
Total Time
Anthony Rietveld
T6, T7, T8
50h
Niels Helderman
T6, T7, T8
50h
Ryan Ramdhan
T9, T10, T11
50h
Jorik Jansen 
T1, T2, T3, T4
50h
Valentijn Verweij
T1, T2, T3, T5 
51h
Nicolas Loaiza
T1, T2, T3, T4
50h
Fiona Moerman
T9, T10, T11
50h
Damian Redegeld
T6, T7, T8
50h
Friso Wiegersma
T9, T10, T11
50h
Elena Schrijvershof
T1, T2, T3, T4
50h


5.1 Task descriptions

Task T1: Research (18h)

Do research about the four error correction methods and outline a programming approach to be able to implement it correctly and efficiently in the Python code and help others in times of need.

Task T2: Error correction Base (10h)

Set up the base of the error correction code in Python, test a basic implementation and make sure everything works correctly. 

Task T3 Error Correction Implementation (20h)

Implement your own part of the error correction code, test your code, track results and analyze. 

Task T4 Setup Github (2h)

Create a repository for push and pull.

Task T5 Working on planning (3h)

Making sure the planning meets the deadlines, keeping everything logged, and correctly documented.


Task T6(15 hours)

Researching the characteristics and possibilities of GNS3 as a tool to set up a network simulation.

Task T7(25 hours)

Working in GNS3 to simulate data centers with a virtual network. 


Task T8(10 hours)

Describing and documenting the work and findings from GNS3.


Task T9( 15 hours)

Doing research and documenting on the different types of data centers and the scaling of the different types of data centers.


Task T10( 15 hours)

Doing research on LANs and routing tables in data centers.


Task T11 ( 20 hours)

Forming multiple data centers types with routing tables on paper and listing the pro’s and con’s.


6 Integration of Learning Goals

6.1 “You know the role of the link layer, where it is implemented, how it relates to the network layer, and what its services and key concepts are.”
This goal is achieved by T1, T6, T7, T9 and T10 ,because this goal has already been partially achieved by the making of our presentation. In these tasks we will further elaborate on this to ensure that we all know what everyone’s project parts entail.

We will research the role of the link layer in T6, T9 and T10. We will implement this in T7 where we use our research to simulate a network of a data center. How this relates to the network layer will be achieved by T10 and T11, where we will research different routing algorithms and use this research to create routing tables that will be used to transmit data in the most efficient way possible.

6.2 “ You know a few simple error detection and correction techniques, and how they are used in practice in the link layer: parity, checksum, CRC.”
This is achieved through T3 and partially through T2 by simulating a connection and fixing the flipped bits through error detection and correction. With the code we wrote in Python.

6.3 “You know the relevance of error detection and correction in systems communicating via channels.”
This goal is achieved by T1 because; all of us will do research towards our subject within the link layer. By reading the provided literature and sheets provided in the lectures. 

6.4 “You know what Hamming distance is, and how it can be used to detect and correct errors.”
This is achieved through T3 and partially through T2 by simulating a connection and fixing the flipped bits through error detection and correction. 

6.5 “You know the mathematical principles underlying CRC (polynomials over finite fields).”
This is achieved through T3 and partially through T2 by simulating an absolutely horrendous connection and fixing the flipped bits through error detection and correction. 

6.6 “You know the multiple access protocols slotted ALOHA and CSMA, and what problem they are solving.”
This is achieved through T11, where we need random access protocols to prevent data collisions when broadcasting data . CSMA will be used to sense the traffic on a channel before transmitting data. It means that if the channel is idle, the station can send data to the channel. Otherwise, it must wait until the channel becomes idle. Using these protocols, any device can transmit data across a network simultaneously when there are data framesets available for transmission.

6.7 “You know what MAC addresses are used for and how the address resolution protocol works.”
This is achieved through T6, because we will use our knowledge of MAC-Addresses and address resolution protocol to create the routing tables of our network simulation. This will make sure that the data is transmitted to the intended receiver.

6.8 “You know the role of link-layer switches, how they compare to routers and how they work.”
This is achieved through T6, because we will apply our knowledge of the link-layer switches to set up a Local Area Network. The switches are used to structure our network and create an efficient way to transmit data. 

6.9 “You know what a data center consists of.”
This is achieved through T6, T7, T9, T10 and T11 combined. Since we both research how GNS3 and Data centers work and experiment with them in GNS3, this will give us an outline for how a data center network is structured which will help us to create such a network using the tools in GNS3. As such we will be able to show what the network consists of through our work.

6.10 “You know what is the job of a border router and that of a load balancer.”
This is achieved through T6, T7, T9, T10 and T11 combined. Since we both research how GNS3 and Data centers work and experiment with them in GNS3, we will find out why border routers and load balancers are important to a data center network's functionality by using them in our simulations.

6.11 “You know how the hierarchical design is used to scale a data center to hundreds of thousands of hosts.”
This is achieved through T7, T9, T10 and T11 combined. We will experiment within GNS3 to create a data center network. In this process and through the research on scaling and GNS3 we will find out why data center networks are structured the way that they are. 

