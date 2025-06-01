# StarStreak-Detector

A lightweight Python-based tool for detecting and classifying astronomical features—stars and streaks—in grayscale .tiff images.

## 🚀 Project Overview

This project was developed to automatically process astronomical images and identify two key features:
- **Stars**: Compact, nearly circular bright spots
- **Streaks**: Elongated trails often caused by satellites or moving objects

The classification is based on contour analysis and aspect ratio, with simple image pre-processing to enhance detection.

## 🧪 Features

- Pre-processes raw grayscale `.tiff` astronomical images
- Applies thresholding and Gaussian blur to isolate features
- Identifies and classifies contours based on area and shape
- Annotates detected features (Star / Streak) with bounding boxes
- Saves and visualises annotated output images

## 🖼️ Example Output

> Detected features will be visualised with green boxes for stars and red boxes for streaks.

![Alt text](./Sample Output/Raw_Observation_001_Set1_detected_feature.png)

## 🛠️ Tech Stack

- Python
- OpenCV
- NumPy
- tifffile
- matplotlib


## 📌 Notes

- Only works with grayscale images
- No machine learning is used — this is a rule-based, classical approach
- Optimised for lightweight, quick feature extraction
