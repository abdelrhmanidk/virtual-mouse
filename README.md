# Virtual Mouse Using Hand Tracking

This project implements a virtual mouse system that allows users to control their laptop mouse without physically touching it. The system utilizes hand tracking with OpenCV and PyAutoGUI to interpret hand gestures and perform mouse actions such as moving the cursor and clicking.

## Features
- Control the cursor by moving your hand in front of the webcam.
- Left-click by pinching your index and middle fingers.
- Smooth movement with customizable sensitivity.
- Easy to extend for additional gestures.

## How It Works
- Hand landmarks are detected using a hand-tracking module.
- The position of the index finger controls the mouse cursor movement.
- Pinching the index and middle fingers together simulates a left-click.

## Installation
To run this project, you'll need the following dependencies:

- OpenCV: `pip install opencv-python`
- PyAutoGUI: `pip install pyautogui`
- Numpy: `pip install numpy`

You can install all dependencies using:

```bash
pip install -r requirements.txt
```
## Usage

- Clone the repository.
- Run the Python script:

```bash
python virtual_mouse.py
```
- Make sure your webcam is active and place your hand in front of it to control the cursor.