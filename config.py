# config.py
# Configuration for 6-Wheel Autonomous Rover

# --- GPIO PIN CONFIGURATION ---
# Assuming L298N or Cytron dual-channel motor driver.
# LEFT_MOTOR_PINS = (Forward Pin, Backward Pin)
LEFT_MOTOR_PINS = (17, 27) 
RIGHT_MOTOR_PINS = (22, 23)

# --- CAMERA CONFIGURATION ---
CAMERA_WIDTH = 320
CAMERA_HEIGHT = 240
CAMERA_FPS = 30

# --- ML MODEL CONFIGURATION ---
# Defaulting to YOLOv4-tiny. Change paths to your specific model files.
YOLO_WEIGHTS = "models/yolov4-tiny.weights"
YOLO_CFG = "models/yolov4-tiny.cfg"

# Confidence threshold for object detection
CONFIDENCE_THRESHOLD = 0.4
# Non-maximum suppression threshold
NMS_THRESHOLD = 0.4
