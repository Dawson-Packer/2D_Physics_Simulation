from application import *
import time
import math
import threading as th


simulation = application("2D Physics Engine", 800, 800)
while simulation.isRunning:
    simulation.tick()
    time.sleep(simulation.delay)