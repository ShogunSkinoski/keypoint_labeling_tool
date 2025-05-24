# Image Keypoint Labeling Tool

Image Keypoint Labeling Tool is a Python desktop application designed for interactive keypoint annotation on images. Built with PyQt5 and OpenCV, it provides a user-friendly GUI to load images, select predefined keypoint sets (such as front or back views), manually adjust keypoint positions, and save the resulting annotations (image metadata and coordinates) to a JSON file.

## Key Features

*   Load images in various formats (any format supported by OpenCV).
*   Select predefined keypoint sets (e.g., "front view" or "back view").
*   Interactive keypoint labeling: Click and drag keypoints to their correct positions on the image.
*   Visual feedback: Displays a skeleton or connections between keypoints overlaid on the image.
*   Save labeled data: Stores image metadata (ID, path, size) and keypoint coordinates in a JSON file.
*   User-friendly GUI developed with PyQt5.

## Setup and Installation

Python 3.x is required.

To install the necessary packages, run the following command in the project directory:
```bash
pip install -r requirements/req.txt
```

## Running the Application

To run the application, execute the following command in your terminal:
```bash
python app/main.py
```
The application window will open. You can then browse for an image file to begin the keypoint labeling process.

## Project Structure

*   `app/`: Contains the core application code.
    *   `app/controller/`: Handles user interactions and application logic.
    *   `app/model/`: Contains data structures, business logic, and data access layers.
    *   `app/view/`: Manages the graphical user interface (GUI).
    *   `app/resources/`: Stores application resources like UI files and data files (e.g., `test.json`).
    *   `app/const/`: Holds constant definitions used across the application.
    *   `app/utils/`: Contains utility functions.
*   `requirements/`: Includes the `req.txt` file for managing project dependencies.
*   `README.md`: This file.

## Future Enhancements

*   Support for different annotation output formats (e.g., COCO, Pascal VOC).
*   Automatic pre-labeling using a pre-trained model.
*   Batch image processing.
*   Customizable keypoint definitions through the UI.
*   Zoom and pan functionality for images.
*   Undo/redo functionality for labeling.
