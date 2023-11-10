"""main.py: Top-level execution file of 2D Physics Simulator"""

__author__ = "Dawson Packer"
__version__ = "1.0"
__status__ = "In-development"

from Application import *
import time
import math
import threading as th
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

simulation = Application("2D Physics Simulator", 800, 800)
while simulation.isRunning:
    simulation.tick()
    time.sleep(simulation.delay)