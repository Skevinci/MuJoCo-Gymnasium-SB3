import numpy as np
import pybullet as p
import pybullet_data
import time

p.connect(p.GUI)
p.resetSimulation()
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.81)
p.setRealTimeSimulation(0)

time.sleep(5)
