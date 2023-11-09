from Application import *
import time
import math
import threading as th
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# TODO: Revise this statement, use standard @<fill in the blank>s
"""
@name 2D Physics Engine
@version 1.0
@author Dawson Packer
@dependencies:
  pygame==2.5.2
"""

simulation = Application("2D Physics Engine", 800, 800)
while simulation.isRunning:
    simulation.tick()
    time.sleep(simulation.delay)