# CV-project
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Hand Sign Recognition Using Computer Vision

## Project Overview

The **Hand Sign Recognition Project** is a real-time computer vision application that detects and recognizes hand gestures using a webcam. The system identifies finger positions and hand movements to perform actions such as **air drawing**, **erasing**, and **gesture-based control** without using any physical input devices.

This project demonstrates the use of **Computer Vision** and **Human–Computer Interaction (HCI)** concepts and is suitable for **2nd–3rd year engineering students**.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Objectives

* Detect hands and fingers in real time
* Recognize different hand signs/gestures
* Enable touchless interaction with the system
* Implement air drawing using hand movements

----------------------------------------------------------------------------

## Technologies Used

* **Programming Language:** Python
* **Libraries:**

  * OpenCV (cv2)
  * NumPy
  * cvzone
  * MediaPipe / HandTrackingModule
* **Hardware Requirement:** Webcam

-------------------------------------------------------------------------------------------------------------

## How the Project Works

1. Webcam captures live video frames
2. OpenCV processes each frame
3. HandTrackingModule detects hand landmarks
4. Finger positions are analyzed
5. Based on the gesture:

   * Drawing is performed
   * Erasing is activated
   * Drawing is stopped
6. A virtual canvas (NumPy array) displays the output

-------------------------------------------------------------------------------------------------------------------------

## How to Run the Project

### Step 1: Install Required Libraries

```bash
pip install opencv-python numpy cvzone mediapipe
```

### Step 2: Run the Program

```bash
python main.py
```

---------------------------------------------------------------------------------------------------------------------

##  Sample Output

* Hand detected on screen
* Drawing appears when specific fingers are raised
* Erasing occurs with a different gesture

-------------------------------------------------------------------------------------------------------------------------

## Advantages

* Touchless and interactive system
* Real-time gesture recognition
* Easy to understand and implement
* No additional hardware required

-----------------------------------------------------------------------------------------------------

## Limitations

* Performance depends on lighting conditions
* Limited number of gestures supported
* Requires a good quality webcam

-----------------------------------------------------------------------------------------------------------------

## Future Enhancements

* Add more hand gestures
* Extend to full sign language recognition
* Integrate with smart devices and applications
* Improve accuracy using deep learning models

--------------------------------------------------------------------------------------------------------

##  Author

**Narmadhadevi D**
B.Tech – Information Technology
St. Joseph’s College of Engineering

---------------------------------------------------------------------------------------------------

## Disclaimer

This project is developed **for educational purposes only**.


