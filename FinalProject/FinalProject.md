
# MyCraft: A Pose Detection Interface for Immersive Gaming

## Introduction

MyCraft transforms the traditional gaming experience by allowing players to interact with Minecraft using intuitive body movements. Leveraging the power of the Mediapipe library and custom Python scripts, MyCraft interprets real-time body movements as in-game controls, offering an immersive and engaging way to play without the need for traditional handheld controllers.

## System Overview

MyCraft's pose detection system uses a camera to capture player movements, which are then interpreted by a Python script running on a Raspberry Pi 4. The script maps these movements to Minecraft controls, enabling a novel way to navigate and interact within the game environment.

## Installation

### Prerequisites

- Raspberry Pi 4 with the latest Raspbian OS
- Compatible camera module for Raspberry Pi
- Python 3.7 or newer
- Minecraft installed on the Raspberry Pi

### Setup Guide

1. Attach the camera to the Raspberry Pi and ensure it is functional.
2. Install the required libraries, including Mediapipe and PyAutoGUI.
3. Obtain the MyCraft script from our repository.
4. Execute the script to start the pose detection.

## Usage

Once MyCraft is running, perform the designated poses within the camera's field of view. The script translates your movements into corresponding Minecraft actions. Ensure you have a clear play area to avoid obstructions and inaccuracies.

## Supported Poses and Corresponding Actions

The following poses are recognized by MyCraft and mapped to Minecraft actions:

- **Walk Forward**: Extend your arms sideways, parallel to the ground.
- **Jump**: Raise both arms straight up.
- **Turn Right/Left**: Extend one arm out to the side, and look in the direction you wish to turn.
- **Look Up/Down**: Tilt your head up or down.
- **Right Click**: Raise your right hand up to shoulder height to perform a 'right-click'.
- **Left Click**: Raise your left hand up to shoulder height to perform a 'left-click'.

<img width="539" alt="Poses" src="https://github.com/zacharypakin/Interactive-Lab-Hub/assets/19901671/c9ae11be-eb4e-4944-a789-59b1c9141ffa">


## Challenges and Solutions

### Latency Issues

Camera data processing latency was initially impacting the gaming experience. We optimized the camera settings, achieving a substantial reduction in latency and more responsive gameplay.

### Pose Overlapping

Certain poses were causing confusion due to their similarity. We refined the detection algorithms and adjusted the sensitivity thresholds to distinguish more effectively between overlapping poses.

### False Positives

To address the issue of false positives, several strategies were implemented:

1. **Confidence Thresholds:** The script utilizes configurable thresholds (`min_pose_detection_confidence`, `min_pose_presence_confidence`, `min_tracking_confidence`) for pose detection and tracking. By setting these thresholds appropriately, poses are only recognized if the confidence level meets or exceeds these values. This approach effectively reduces the likelihood of false positives, ensuring that only poses detected with sufficient confidence trigger corresponding actions.

2. **Specific Pose Detection Conditions:** To further enhance accuracy, the code includes functions with precise conditions for identifying specific poses (such as `is_left_arm_raised`, `is_right_arm_raised`). These functions evaluate the relative positions of key landmarks (like wrists and ears for raised arms) to confirm a pose. This method ensures that only clearly defined, intended poses activate the system.

3. **Real-time Processing:** The system processes video frames in real-time, continuously updating pose detection. While this feature does not directly reduce false positives, it allows for rapid correction and adjustment in subsequent frames, thus minimizing the impact of any incorrect pose detection.

4. **Status Checks Before Action:** Before triggering actions, the code checks for changes in the status of a pose (e.g., from not raised to raised). This check helps in reducing repetitive actions for the same pose detection and indirectly lessens the chance of transient false positives affecting the system.

## Design Process

### Conceptualization and Initial Research

- **Idea Generation:** 
  - The journey of MyCraft began with exploring innovative ways to transform gaming experiences. We were captivated by the idea of using body movements as game controls, leading us to delve into the potential of pose detection technology.

- **Research Phase:** 
  - In-depth research into pose detection technologies was undertaken. Mediapipe was chosen for its robust capabilities and adaptability, ideal for the complex task of real-time pose recognition in gaming.

### Prototyping and Development

- **Early Prototyping:** 
  - The initial prototype, developed with Python and Mediapipe, focused on mapping simple gestures to keyboard inputs. This stage was crucial for gaining an understanding of the practical application of pose detection in gaming.

- **Core Feature Development:** 
  - We expanded the prototype to include a wider range of gestures, meticulously refining their correlation with specific Minecraft controls. This phase involved intensive coding and was pivotal in translating physical movements into virtual game actions.

### Iterative Testing and Refinement

- **User Testing:** 
  - Conducting user testing sessions was integral to our development process. These tests provided essential feedback on the system’s accuracy and responsiveness, highlighting issues such as latency and pose overlapping.

- **Algorithm Refinement:** 
  - The pose detection algorithms underwent continuous refinement, heavily influenced by user feedback. We focused on improving the accuracy of the system and reducing the occurrence of false positives.

- **Evolution of Pose Detection Techniques:** 
  - Our early attempts at pose recognition involved complex algorithms designed to capture detailed body movements. However, we soon discovered that simpler methods were more effective. For instance, using straightforward criteria like determining if a wrist was above an ear allowed for easier and more reliable pose recognition.

- **Selection of Poses:** 
  - The final set of poses was chosen through an iterative process, guided by user feedback. Our objective was to identify poses that were distinct yet natural and intuitive.

### Final Integration and Testing

- **Feedback Integration and Comprehensive Testing:** 
  - The final stage involved integrating all improvements and conducting extensive testing. We ensured the system was robust and user-friendly, capable of handling a variety of scenarios and user interactions.


## Project Timeline Plan:

- **Nov 14**: Finalize the design for pose detection parameters. Begin collecting diverse movement data for pose detection.
- **Nov 21**: Develop the initial code for pose-to-key input mapping. Start testing with basic pose detection.
- **Nov 28 & 30**: Refine pose detection algorithms. Test functionality and accuracy. Integrate camera for enhanced pose detection.
- **Dec 2**: Implement and test camera-based pose detection system. Adjust algorithms based on initial user feedback.
- **Dec 4**: Finalize the integration of the camera-based pose detection system. Conduct comprehensive testing with users of varying movement patterns and gaming styles. Refine the user experience based on test results.

## Future Improvements

- **Performance**: Optimize pose detection algorithms to further reduce latency.
- **Pose Differentiation**: Enhance algorithms for increased accuracy in differentiating similar poses.
- **User Calibration**: Introduce user-specific calibration to tailor pose recognition to individual players.

## Team and Work Distribution

In our project, the collaboration and distinct contributions of each team member were key to its success. Zack Pakin led the way with his insightful concept, integrating Minecraft on Pi with MediaPipe to enhance user interaction. Carlos Suberviola applied his technical acumen to address software integration challenges, ensuring a smooth and functional user interface. Ivan Nikitovic contributed significantly with his expertise in pose detection, elevating the game's interactivity and user engagement. Finally, Neel Patil was instrumental in developing the game's logic, crafting an engaging and coherent gameplay experience. As a team of students, each member's unique skills and perspectives were invaluable in transforming our initial concept into a functional and engaging project. Our collaborative approach allowed us to learn from each other and navigate the complexities of the project, highlighting the importance of teamwork in achieving our goals.

## Conclusion

MyCraft is a pioneering interface that offers a new level of interaction with Minecraft. The project has demonstrated the potential of pose detection in gaming and presents exciting opportunities for future development and refinement.

## Images
![IMG_3394](https://github.com/zacharypakin/Interactive-Lab-Hub/assets/19901671/bde8a165-b962-4d9b-94db-42ecd8ed5d67)
![IMG_3393](https://github.com/zacharypakin/Interactive-Lab-Hub/assets/19901671/1a912dd7-5966-4db9-b717-7b0e565495b7)
![IMG_3392](https://github.com/zacharypakin/Interactive-Lab-Hub/assets/19901671/ba360d23-4b28-4cfd-b053-86df359e0f6a)



## Video Demonstration

Watch MyCraft in action: [MyCraft Video Demo](https://drive.google.com/file/d/15PhXiFeDBuu0YOuQx1pM1F5UVeHfn6qg/view?usp=sharing)


## Team Reflections

Reflecting on our journey with MyCraft, the beginning of this project was quite daunting. We were faced with a challenge that resembled a complex puzzle, with countless pieces scattered and no clear starting point. This overwhelming sense of complexity initially made the project seem insurmountable, as if we were venturing into uncharted territories far beyond our capabilities.

However, as we delved deeper into the development process, the confusion began to dissipate. Each challenge we overcame brought clarity and understanding, transforming what initially appeared as an unachievable task into a series of manageable steps. This gradual unraveling of complexities not only made the project feasible but also fueled our motivation to push the boundaries of what we could create.

This experience taught us a valuable lesson: never be deterred by the initial overwhelming nature of a complex task. It's the momentum that counts. Once we set the wheels in motion, each step forward seemed to align the pieces of the puzzle, proving that even the most daunting tasks can be tackled methodically, one step at a time.




          
