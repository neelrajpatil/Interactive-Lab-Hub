
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

False positives were reduced by requiring poses to be held for a short duration before being registered, preventing inadvertent action triggers.

## Design Process


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

## Conclusion

MyCraft is a pioneering interface that offers a new level of interaction with Minecraft. The project has demonstrated the potential of pose detection in gaming and presents exciting opportunities for future development and refinement.

## Images
![IMG_3394](https://github.com/zacharypakin/Interactive-Lab-Hub/assets/19901671/bde8a165-b962-4d9b-94db-42ecd8ed5d67)
![IMG_3393](https://github.com/zacharypakin/Interactive-Lab-Hub/assets/19901671/1a912dd7-5966-4db9-b717-7b0e565495b7)
![IMG_3392](https://github.com/zacharypakin/Interactive-Lab-Hub/assets/19901671/ba360d23-4b28-4cfd-b053-86df359e0f6a)



## Video Demonstration

Watch MyCraft in action: [MyCraft Video Demo](https://youtube.com)

## Team Reflections

Our team embarked on this project with the vision of enhancing the gaming experience. Throughout the development, we've learned the importance of iterative testing and user feedback. If we were to start over, we would place even greater emphasis on early-stage user testing to refine our pose detection algorithms from the onset.
