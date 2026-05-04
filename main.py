import time
from motor_controller import MotorController
from vision_ml import VisionSystem
from navigation import NavigationEngine

def main():
    print("Initializing Rover Systems...")
    try:
        motors = MotorController()
        vision = VisionSystem()
        nav = NavigationEngine(motors)
        
        print("Rover is active. Press Ctrl+C to stop.")
        while True:
            # 1. Capture and analyze environment
            obstacles = vision.detect_obstacles()
            
            # 2. Make navigation decision
            nav.process_obstacles(obstacles)
            
            # Short sleep to prevent CPU hogging and allow thread switching
            time.sleep(0.05)
            
    except KeyboardInterrupt:
        print("\nShutting down rover...")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
    finally:
        # Graceful shutdown to prevent runaway motors
        if 'motors' in locals():
            motors.stop()
        if 'vision' in locals():
            vision.release()
        print("Shutdown complete.")

if __name__ == "__main__":
    main()
