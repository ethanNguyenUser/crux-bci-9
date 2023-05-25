# CruX BCI Team 9 GitHub Repository

## Poster
![Poster](https://github.com/ethanNguyenUser/crux-bci-9/blob/main/BCI%20Poster/1.png)

## [Presentation Format](https://docs.google.com/presentation/d/1BqtsrBfNDqGUVem8tdIMUvQsRFDbliThsNez5g8zBbo/edit#slide=id.p)

## Proposal
[Google Doc Version of Proposal](https://docs.google.com/document/d/1CXb2ZEh6SnwkfzvR8MbCsqIKvdNNTY0F7p7aPkmKjRU/edit?pli=1)

## Context-Dependent Control of Robotics Systems (CDCRS)

### Narrative
The goal of our project is to enable subjects to provide directional input to their BCI to control a robotics system, and when they think to flick a “switch,” they may switch to controlling a different system that uses the same underlying directional inputs. We plan to have the directions of “left, right, down, and up” as well as the 5th “context switch” control for a total of five inputs the BCI will have to map to from EEG readings. The two main “programs” that the subject may switch between are the robotic arm mode and electric wheelchair mode. Past BCI’s that manipulate a certain robotic component are more niche and their applications, sticking to one device to be controlled at a time. CDCRS may allow for paralyzed patients to both traverse and manipulate their environment by either controlling the electric wheelchair or robotic arm, respectively. Past research (nature.com/articles/srep38565) has also shown that it is possible to produce categorizable EEG signals that only rely on the subject thinking in certain directions by motor imagery, which would be an improvement over requiring visual attention of a screen to elicit a signal.

### Overall Aim
To develop a BCI that uses subjects’ motor imagery signal readings to control a virtual cursor that enables directional input and context-switching between controlling either a robotic arm or electric wheelchair.
  
### Specific Aims
IDevelop a robust software that can detect a subject’s inputs to switch between program contexts: We will design a software that based on EEG readings from the BCI, can robustly detect a ‘switch’ action which can transfer a user’s input from one device to another. In our case, we hope this will be from a robotic arm to a wheelchair prototype and vice versa. The robustness of our software will be a key priority, as the value of this capability would be, in large part, based on its reliability. This program will also read-in directions by having the subject think in the desired directions after sufficient training of the model.
- Control a robotic arm using a virtual cursor: We plan to use the directional input from the EEG readings to map the 2D translational position of the end-effector using inverse kinematics in a plane. We will have to establish a suitable sensitivity for the model, to take into account reaction time of the robotic arm and noise/variability in our EEG readings. 
- Control a proof-of-concept prototype for an electric wheelchair using a virtual cursor: We hope to map directional inputs to simple one axis of translational movement and one axis of rotational movement for a wheelchair prototype using a constant-force model. We will have to establish a suitable sensitivity for the model to take into account the reaction time of the wheelchair prototype and noise/variability in our EEG readings.

### Significance
Context-Dependent Control of Robotics Systems (CDCRS) would enable paralyzed and disabled patients to replace loss of function(s) in:
Movement: patients could control an electric wheelchair for transportation
Dexterity: patients could control a robotic arm to perform basic object manipulation tasks like grabbing and holding food for instance
Extensibility: CDCRS would be nicely suited to be extended upon by other developers adding their own programs to control other systems that rely on directional input. Some ideas are:
- A virtual cursor to browse the web
- A communication tool (perhaps a texting app that uses a flick-input scheme youtube.com/shorts/BhD6r8NKlmY)
- A drawing board
- A drone/RC vehicle
Musical instruments

### Approach
We will primarily be following the methods outline in the 2016 paper, “Noninvasive Electroencephalogram Based Control of a Robotic Arm for Reach and Grasp Tasks” (nature.com/articles/srep38565#Sec17), which demonstrates the control of a robotic arm using the BCI 2000 software’s virtual cursor feature.
Data will be collected on 2-3 subjects, and we may try having the subjects train to variate sensorimotor rhythm by instructing them to think to move in certain directions in their hands and categorizing the recorded EEG data signals relative to the instructions given.
If we have extra time, we will also consider coding the machine learning model from scratch using the various Python libraries (tensorflow and PyTorch) that were taught to us in the Fall workshop. The drawback to creating our own machine learning model would obviously be the extra time needed to understand and debug our own program, whereas the BCI 2000 software comes for free, is tested for bugs, and is proven to be compatible with controlling robotic systems live. The benefits however of creating our own model is perhaps greater customizability in our program, as there may be certain features that we want that would be harder to add by editing someone else’s code rather than our own (the code is open source, so that is an option). BCI 2000 is also an .exe program, so it isn’t native to MacOS, which may make it harder for members with only Mac’s to easily use the software.

### Experimental Design Proposal
#### Question
How can we create a program context-switching software reliant only on a subject’s thoughts? If such a software is created, what are some of the applications to assistive technology, and how could this software be effectively utilized by impaired subpopulations?
#### Hypothesis
A brain computer interface that allows for robust context-switching between two modes–controlling a robotic arm for object manipulation and controlling an electric wheelchair for environment traversal–can be developed by analyzing signals produced by the subject’s motor imagery.
#### Metrics
##### Accuracy of responsiveness:
To be an effective aid the BCI integrated software would need to have a high accuracy of responses, as it would need to perform tasks routinely. This can be measured through the level of accuracy of a subject’s desired response, versus the actual recorded response.
##### Speed:
In order for assistive technology to be effectively applied and used by people, it must have a high speed. This can be measured as the time delay between thought and the desired action running. We may also compare our BCI efficacy against a control who simply uses a physical controller/keyboard to control the robotic system.
If a bias is introduced, we should create the software such that it is averse to false positives: preferable to find difficulty to switch rather than spontaneously switch without command

### Accuracy of responsiveness
#### How accurately am I able to evaluate this metric?
This metric can’t be measured with extreme accuracy as it isn't able to be quantified, as opposed to other metrics like speed. The only useful numeric statistic derived from an experiment on this metric would be the percentage of accuracy (that is, how often the response matches the desired outcome). 
Alternatively, we can measure the degree to which the system is accurate; this may be difficult to do with more advanced movements, but for simpler objectives, we can measure the distance it is off by, etc. 
#### Are there multiple methods of evaluating this metric?
Yes, we can do a 2-measurement system where the response is either correct or incorrect. We can also measure the degree to which responses are accurate as stated above. This can be done in multiple ways such as distance off from desired position, functioning to a certain degree (such as 3 fingers moving when a fist was desired), and how long the software can maintain the desired output (length of accuracy). 
#### How controllable are the factors that may cause variability in this metric?
It is possible that, apart from the actual software, that human subjects can result in variability. (demographically, we can consider physical age, (mental age? not sure how that would be measured reasonably) level of neurological function, etc.). If we primarily use people who are working on the software itself, it could very reasonably be controlled, as they will be most familiar with it. (Consider, also, the level of communication needed for people unfamiliar with the software to properly use it…does it require very specific instructions or will it be built to be more intuitive?) 
### Experiment Proposal
1. Train a model to interpret motor-imagery commands using BCI 2000 to control a virtual cursor for inputs to the electric wheelchair and robotic arm.

![Virtual Cursor](https://github.com/ethanNguyenUser/crux-bci-9/blob/main/Pictures/virtualCursor.png)

*Figure 1. Virtual Cursor setup*

  - The subject will move the virtual cursor by using the BCI 2000 cursor module. When the cursor touches the regions denoting one of the four directional inputs, the BCI will register that as an input and continue holding that input
Measure accuracy and speed of the robotic arm using PsychoPy protocols on a subject using the BCI
 - Instruct the subject to prioritize accuracy over speed when conducting the following trials.

![PsychoPy GUI](https://github.com/ethanNguyenUser/crux-bci-9/blob/main/Pictures/psychoPyInstructions.png)

*Figure 2. Example instructions from PsychoPy GUI*

  - Prompt the subject with one of the following random commands: “Move system right,” “Move system left,” “Move system up,” “Move system down”
  - For the duration of the command being shown, the subject continuously tries to move the robotic system in this direction using motor imagery.
  - Record accuracy as a time-measure comparing when: instruction A is being shown to subject vs. output A is being recorded by the BCI. 
  - Record the time between when the movement commands are issued vs. when the robotic system moves
  - After at least four or so movement commands (there will be a random amount more, perhaps up to ten commands total), prompt the subject to switch contexts to control the other robotic system.
  - Record the time it takes for a context to be switched and whether there were other commands issued between the instruction and the context switch
  - Repeat steps b-f 15 times (should take about 10 minutes) for a total of 15 context switches
  - Average the accuracy of time spent on the right movement command over the 100 trials, which may be called the “Movement Accuracy Metric”
  - Average the time for each movement command over the 100 trials, which may be called the “Movement Response Time Metric”
  - Average the the accuracy and time spent to complete the Context Switch command, which may be called the “Context Switch Response Time Metric”
3. Measure accuracy and speed of the robotic arm using PsychoPy protocols on a control subject not using the BCI
  - Have the control subject use a real mouse instead of a virtual cursor to repeat the PsychoPy protocol.
  - Tweak the BCI based on comparisons between the control subject and the BCI-subject as well as by using the other objective measurements of speed/accuracy not based on comparison.


4.
  - Context-switching 
  - 2D movement in 4 main directions
  - Detail how the experiment will test the hypothesis.
    - Subjects will be shown flashcards of various commands and think of that command (ex. switch to prosthetic right arm, move left, move up). Measure the outcome (accuracy, speed, etc.).
  - Discuss possible outcomes ahead of time and what they would mean with respect to the hypothesis.
    - If the response is the desired outcome, the context switching and 4 directional movement program are effective
  - Detail potential confounding factors, biases, or other logical flaws with the experimental design and explain why they cannot be addressed or how to best address them.
    - We will have to address the problem of ‘probability’, because the model that we train to process our EEG data to decide on a directional output will essentially be deciding on these outputs based on a probability of accuracy. If we make this threshold very low, it is likely that we have a directional output which is unsteady/not continuously directed and probably quickly alternates between directions. On the other hand, we do not want it to be an exhaustive process for a continuous directional output, and we would like to reduce lag. 

### Data Flow
What is eliciting a signal from the subject? 
When measuring the accuracy and speed metrics, the subject is creating the signal to manipulate the BCI device based on our instructions from PsychoPy. From the rounds of training where the software will learn to differentiate between the subjects’ different cues of direction, 

How are you physically collecting the signal from the subject?
The signal is coming from an EEG headset and feeding back to our software. We will specifically be monitoring the C3 and C4 electrodes and surrounding electrodes to target the motor sensory cortex. A past paper has demonstrated that these electrodes are ideal candidates for enabling the motor sensory imagery technique (nature.com/articles/srep38565#Sec17)

How/what is communicating the signal digitally?
The signal should be digitized by the OpenBCI Cyton Board as it converts the electrical signals from the cap to signals to be sent over bluetooth by the dongle to the OpenBCI GUI software.
Is the signal filtered? Digitally? Physically?
The signal will be filtered by applying a butterworth filter on frequencies ranging from 1 Hz to 58.5 Hz, which exclude the noisy 60 Hz and 120 Hz frequencies generated from power lines/wall sockets.
How is the signal being organized/restructured? What is doing it?
We would like to categorize EEG data to 4 directional outputs using the signals generated. There should be sufficient difference between the patterns in the EEG to allow for the BCI 2000 software enough distinction of signals to control the virtual cursor (ieeexplore.ieee.org/document/1300799). We may also train a ML model ourselves that can robustly differentiate between the subject’s intent to move in certain directions.

What is processing the signal? How is it being processed?
The BCI 2000 software is processing the signals generated by the OpenBCI cap. From the article: “Most adults display 8–12 Hz (i.e., μ) and/or 18–26 Hz (i.e., β) rhythms in the EEG recorded over primary sensorimotor cortices. Normally, these sensorimotor rhythms show amplitude increases and decreases that are related to sensory input and/or movement or movement imagery (see [40] and [41]). Many studies have demonstrated that humans can learn to control μ or β rhythm amplitudes independent of actual movement and use that control to move a cursor to targets on a computer screen (e.g., [2], [4], [5], and [42]– [44])” (ieeexplore.ieee.org/document/1300799).
We will be focusing on the upper μ-band frequencies (10-14 Hz) using a bandpass filter and then sending it to the BCI 2000 CursorTask module

Is the signal stored for any reason? How is the stored signal structured? Is it raw or processed?
For the training session, the subject’s signals will be stored to later be processed and categorized possibly if we decide to write the analysis portion of the code ourselves

Is the signal part of a feedback loop?
Indirectly yes, as the signal generated by the user will induce a change in the robotic system the subject is attempting to control, and so the user will have to react to this changing system mostly by visual feedback in order to better guide the robotic manipulation.

![Data Flow Diagram](https://github.com/ethanNguyenUser/crux-bci-9/blob/main/Pictures/dataFlow.png)

*Figure 3. Diagram showing the directions data will be sent between the hardware/software*

### References
Noninvasive Electroencephalogram Based Control of a Robotic Arm for Reach and Grasp Tasks: nature.com/articles/srep38565
BCI 2000: ieeexplore.ieee.org/document/1300799
BCI softwares: https://sccn.ucsd.edu/~scott/pdf/Brunner_BCI11.pdf
BCI 2000 Cursor: https://www.bci2000.org/mediawiki/index.php/User_Reference:CursorTask
OpenBCI Motor Imagery doc: docs.openbci.com/Examples/EEGProjects/MotorImagery/
