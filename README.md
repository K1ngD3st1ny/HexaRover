# HexaRover: 6-Wheel Autonomous Rover

HexaRover is a Python-based autonomous navigation system for a 6-wheel rover powered by a Raspberry Pi 4 Model B. It uses an onboard Raspberry Pi Camera and OpenCV with a lightweight YOLO model to perform real-time object detection and dynamic obstacle avoidance.

## 🚀 Features
- **Skid-Steer Locomotion**: Controls 6 DC motors (wired in parallel as left and right banks) using `gpiozero` for smooth tank-like movement.
- **Computer Vision**: Leverages OpenCV's DNN module and YOLO (e.g., YOLOv4-tiny) for fast, CPU-bound object detection.
- **Multithreaded Processing**: Runs the camera capture on a background thread to maintain high frame rates and prevent the main control loop from blocking.
- **Intelligent Navigation**: Parses bounding boxes from the vision system to determine obstacle proximity and position, executing evasive maneuvers when necessary.

## 🛠️ Hardware Requirements
- Raspberry Pi 4 Model B
- 6x DC Motors
- Dual-channel Motor Driver (e.g., L298N or Cytron)
- Raspberry Pi Camera Module (CSI)
- Battery Pack (e.g., 7.4V LiPo or 12V depending on motors)
- Jumper wires & chassis

## 📋 Wiring & Pinouts
For detailed instructions on how to wire the motor driver, motors, and camera to the Raspberry Pi GPIO pins, please refer to the **[WIRING.md](WIRING.md)** document.

## 💻 Installation

1. Clone this repository to your Raspberry Pi:
   ```bash
   git clone https://github.com/K1ngD3st1ny/HexaRover.git
   cd HexaRover
   ```

2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. **Machine Learning Model Setup**:
   The system is configured to use YOLO object detection. You need to provide the weights and config files.
   - Download a lightweight model like `yolov4-tiny.weights` and `yolov4-tiny.cfg`.
   - Place them in a `models/` directory inside the project folder, or update the `YOLO_WEIGHTS` and `YOLO_CFG` paths inside `config.py`.

## 🚦 Usage

Once your hardware is wired and dependencies are installed, start the rover by running:

```bash
python main.py
```

> **Warning:** Always test the rover while it is lifted off the ground to verify the wheels rotate in the correct direction and respond to camera input properly before putting it on the floor!

## 📂 Project Structure
- `main.py`: The core event loop that orchestrates vision, decision-making, and motor control.
- `vision_ml.py`: Handles threaded camera capturing and YOLO inference.
- `navigation.py`: The logic engine that decides how to move based on obstacles.
- `motor_controller.py`: Low-level wrapper for `gpiozero` motor control.
- `config.py`: Centralized configuration for GPIO pins, camera resolution, and model paths.
