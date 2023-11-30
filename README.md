# ML_Movie
# README

## Introduction

Welcome to this GitHub repository! This project utilizes the latest GPT-4 model from OpenAI to generate high-quality datasets, focusing on detailed descriptions of each frame in movie scenes, including the structure of the scene, camera angles, actors, emotions, and plot elements.

## Important Updates

- **Adoption of the New GPT-4 Model:** We've shifted to the newly released GPT-4 model by OpenAI, resulting in significant improvements in the quality of our datasets.
- **Code Updates:** All related codes for dataset generation have been updated and are now centralized in `man.py`.
- **Discontinuation of Previous Installation and Setup Processes:** We are in the process of revising our installation guidelines.

## Accessing Dataset and Models

If you wish to access our dataset and the fine-tuned Stable Diffusion model, please visit our [Hugging Face repository](#). (Replace `#` with the actual URL to your Hugging Face repository)

## Model Demonstrations

Below are demonstrations of the results from our fine-tuned model compared to the non-fine-tuned model:


### testing text:
"The image provided appears to be an underwater shot, presumably of the bow of the RMS Titanic as it lies on the ocean floor. Unfortunately, due to the darkness and the low resolution in the image, specific details are not clearly visible.
In scenes such as this in the movie ""Titanic,"" characters would typically be situated in a submarine or remotely operated vehicle (ROV), exploring the wreckage of Titanic. The spatial relationship between characters during these explorations would typically involve the characters inside the submersible looking out at the shipwreck and directing the ROV to maneuver around the ship's remains.
The subtitle, ""Okay, take her up and over the bow rail,"" suggests that someone is instructing a remote operator or a pilot of a submersible to navigate the vehicle in a specific manner around the ship's wreckage. This instruction would mean that the vehicle should ascend and move over the bow rail of the ship's wreckage, which is a part of the ship's structure at the front.
The spatial relationship in this context involves the remote vehicle moving in the water relative to the massive, stationary wreck of the Titanic. This movement is part of the explorative plot in the movie where the characters are investigating the remains of the sunken ship.
In the scene, elements that would typically be in the foreground include the illumination from the vehicle's lights and possibly parts of the vehicle itself. In the background, you would usually see parts of the shipwreck bathed in the eerie glow of the submersible's lights, giving the audience a sense of the ghostly, haunting atmosphere of the deep ocean and the tragedy that occurred there. The layout enhances the emotional impact of the film by conveying a sense of exploration, historical intrigue, and the somber reality of the Titanic's fate."
### Fine-Tuned Model
![Fine-Tuned Model](1.2.png)
![Fine-Tuned Model](2.1.png)
### Non-Fine-Tuned Model
![Non-Fine-Tuned Model](1.1.png)
![Non-Fine-Tuned Model](2.2.png)

## Installation Instructions

The new installation guide is currently being developed. Depending on your computer's environment, you may need to add various database dependencies. We will provide a detailed installation and configuration guide as soon as possible.

## Dataset Changes

- **Discontinuation of MovieNet Database:** We've completely abandoned the MovieNet database as the datasets generated with the GPT-4 model are far superior in clarity and accuracy.
- **Improved Clarity and Accuracy:** The data generated by the GPT-4 model is not only clearer but also more precise in descriptions.

## Branch Information

- **Demo Branch:** You can view the old code in the Demo Branch.
- **Main Branch:** The new version of the code will be continuously refined and iterated in the Main Branch.

## Usage

1. Clone the repository to your local machine.
2. Ensure Python and the required libraries are installed (installation guide is being updated).
3. Run `man.py` to generate the dataset as per the instructions.

## Contribution

Contributions to this project are welcome, either through submitting Pull Requests to improve the code or functionality, or by submitting new ideas or bug reports through Issues.
