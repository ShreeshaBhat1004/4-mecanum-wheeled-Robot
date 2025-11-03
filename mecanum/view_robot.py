import pybullet as p
import pybullet_data
import time

# 1. Setup the simulation
physicsClient = p.connect(p.GUI)  # Connect to the GUI
p.setAdditionalSearchPath(pybullet_data.getDataPath())  # To load the plane
p.setGravity(0, 0, -9.81)

# 2. Load the ground plane
planeId = p.loadURDF("plane.urdf")

# 3. Load your robot
#    We spawn it slightly above the ground (0.1m)
robot_start_pos = [0, 0, 0.1]
robot_start_orientation = p.getQuaternionFromEuler([3.14159, 0, 0])

print("Loading robot from mecanum_bot.urdf...")
robotId = p.loadURDF("mecanum.urdf", 
                     robot_start_pos, 
                     robot_start_orientation)

print("Robot loaded successfully.")

# 4. Run the simulation
#    This loop keeps the simulation window open
try:
    while True:
        p.stepSimulation()
        time.sleep(1./240.)
except KeyboardInterrupt:
    print("\nSimulation stopped.")
    p.disconnect()
