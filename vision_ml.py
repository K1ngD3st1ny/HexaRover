import cv2
import threading
import os
import config

class VisionSystem:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, config.CAMERA_WIDTH)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, config.CAMERA_HEIGHT)
        self.cap.set(cv2.CAP_PROP_FPS, config.CAMERA_FPS)
        
        self.running = True
        self.frame = None
        self.lock = threading.Lock()
        
        # Check if model files exist, otherwise don't crash but print a warning
        if os.path.exists(config.YOLO_WEIGHTS) and os.path.exists(config.YOLO_CFG):
            self.net = cv2.dnn.readNet(config.YOLO_WEIGHTS, config.YOLO_CFG)
            # Use CPU for inference on Pi
            self.net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
            self.net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
            self.model = cv2.dnn_DetectionModel(self.net)
            self.model.setInputParams(size=(320, 320), scale=1/255, swapRB=True)
            self.model_loaded = True
        else:
            print(f"Warning: YOLO files not found at {config.YOLO_WEIGHTS} or {config.YOLO_CFG}. Vision will be skipped.")
            self.model_loaded = False
        
        # Start background thread for frame capture
        self.thread = threading.Thread(target=self._update, daemon=True)
        self.thread.start()

    def _update(self):
        while self.running:
            ret, frame = self.cap.read()
            if ret:
                with self.lock:
                    self.frame = frame

    def get_latest_frame(self):
        with self.lock:
            if self.frame is not None:
                return self.frame.copy()
        return None

    def detect_obstacles(self):
        if not self.model_loaded:
            return []
            
        frame = self.get_latest_frame()
        if frame is None:
            return []
        
        classes, scores, boxes = self.model.detect(frame, config.CONFIDENCE_THRESHOLD, config.NMS_THRESHOLD)
        
        obstacles = []
        # If no objects are detected, detect() returns empty tuples or lists
        if len(classes) == 0:
            return obstacles
            
        for (classid, score, box) in zip(classes, scores, boxes):
            x, y, w, h = box
            
            # Find approximate horizontal position: left, center, right
            center_x = x + w / 2
            position = "center"
            if center_x < config.CAMERA_WIDTH / 3:
                position = "left"
            elif center_x > 2 * config.CAMERA_WIDTH / 3:
                position = "right"
                
            obstacles.append({
                "box": box,
                "score": score[0] if isinstance(score, (list, tuple)) else score,
                "position": position,
                "width": w,
                "height": h
            })
            
        return obstacles

    def release(self):
        self.running = False
        self.thread.join()
        self.cap.release()
