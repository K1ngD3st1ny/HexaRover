import config

class NavigationEngine:
    def __init__(self, motors):
        self.motors = motors
        
    def process_obstacles(self, obstacles):
        if not obstacles:
            # Path is clear
            self.motors.move_forward()
            return
            
        # Find the largest (closest) obstacle based on bounding box area
        closest = max(obstacles, key=lambda o: o['width'] * o['height'])
        
        area = closest['width'] * closest['height']
        frame_area = config.CAMERA_WIDTH * config.CAMERA_HEIGHT
        
        # If the obstacle occupies more than 40% of the screen, it's dead ahead and close
        if area > frame_area * 0.4:
            self.motors.stop()
            self.motors.move_backward(0.5)
            # Evade by turning
            self.motors.turn_right(1.0)
            return
            
        # Simple avoidance logic based on position
        if closest['position'] == "left":
            self.motors.turn_right(0.8)
        elif closest['position'] == "right":
            self.motors.turn_left(0.8)
        else: # center
            self.motors.stop()
            self.motors.turn_right(1.0)
