import numpy as np
import pybullet as p
import pybullet_data
import time
import os

p.connect(p.GUI)
p.resetSimulation()
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.81)
p.setRealTimeSimulation(0)

# load assets
current_dir = os.getcwd()
urdf_path = os.path.join(current_dir, 'jaka_zu3_URDF.urdf')
planeId = p.loadURDF("plane.urdf", [0, 0, 0], [0, 0, 0, 1])
robotId = p.loadURDF(urdf_path, [0, 0, 0], [0, 0, 0, 1], useFixedBase=1)

time.sleep(5)
