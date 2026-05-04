from gpiozero import Robot
import config

class MotorController:
    def __init__(self):
        # We use gpiozero.Robot for skid-steer style control.
        # It takes left and right motor pin tuples (forward, backward).
        self.robot = Robot(left=config.LEFT_MOTOR_PINS, right=config.RIGHT_MOTOR_PINS)
    
    def move_forward(self, speed=1.0):
        self.robot.forward(speed)
        
    def move_backward(self, speed=1.0):
        self.robot.backward(speed)
        
    def turn_left(self, speed=1.0):
        self.robot.left(speed)
        
    def turn_right(self, speed=1.0):
        self.robot.right(speed)
        
    def stop(self):
        self.robot.stop()
