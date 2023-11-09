# 2D Physics Simulation `v1.0`

A physics simulation written in Python that calculates the response of objects to interactions in a 2D space. This is done so by applying the laws governing impulse, conservation of momentum, and conservation of energy.

## Setup

The GUI is built in pygame, which can be installed via running the following command in the current directory: 

    pip install -r requirements.txt

Start the application:

    python main.py

## Usage

As of *11/8/2023*, the simulation works without user input, and runs indefinitely until closed. A finite number of objects, called `CollisionObjects`, are created and simulated according to the following flow chart:

![image][flowchart_img]








[flowchart_img]: docs/documentation/flowchart.png