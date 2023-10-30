from Application import *
import time
import math
import threading as th


simulation = Application("2D Physics Engine", 800, 800)
while simulation.isRunning:
    simulation.tick()
    time.sleep(simulation.delay)