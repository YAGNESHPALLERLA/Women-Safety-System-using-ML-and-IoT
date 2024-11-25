# Women Safety System Using ML and IoT

## Overview
The *Women Safety System* is a robust, IoT-enabled solution that utilizes machine learning algorithms to detect emergencies and provide real-time assistance. This system combines wearable sensors, location tracking, and ML models to identify distress and notify pre-configured contacts via SMS or other communication methods.

## Features
- **Real-time Emergency Detection**: Uses machine learning to classify distress based on sensor data.
- **Location Tracking**: Provides real-time GPS coordinates to aid responders.
- **SMS Alerts**: Sends emergency messages directly to pre-defined contacts.
- **Portable IoT Hardware**: Integrates easily with wearable devices.
- **Customizable**: Easily adaptable for additional features or target groups.

## Architecture Overview
The system consists of the following components:
1. **Hardware**:
   - Wearable sensors (e.g., accelerometer, GPS).
   - Microcontrollers like ESP32 for data transmission.
2. **Machine Learning**:
   - Trained ML models for emergency classification.
3. **Software**:
   - Python scripts for data processing, classification, and alert notifications.
4. **Communication**:
   - Serial communication and GSM module integration for SMS alerts.

![Architecture Diagram](path/to/diagram.png) *(Replace with actual diagram)*

## Dataset
- **Source**: Data collected from wearable sensors during various simulated scenarios.
- **Preprocessing**: Outlier removal, normalization, and feature extraction.
- **Labels**: Distress (1) and Normal (0).

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/YAGNESHPALLERLA/Women-Safety-System-using-ML-and-IoT.git
   cd Women-Safety-System-using-ML-and-IoT
   
2. Set up hardware:
- Connect sensors to the microcontroller as per the schematics.
- Configure GSM module for sending SMS.
  
3. Run the system:
   ```bash
   python main.py
