import pygame as pygame
import math as math
import os
import random

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Object(pygame.sprite.Sprite):
    def __init__(self, height: int, width: int, x: int, y: int,\
                  r: float, id: int, file_name: str, name: str):
        """
        @brief    Base class Object used to store basic data for elements loaded to the screen or
                  running in the background.
        @param height    The height of the sprite to draw.
        @param width    The width of the sprite to draw.
        @param x    The x-position on the screen of the object.
        @param y    The y-position on the screen of the object (top-down).
        @param r    The rotational value of the object.
        @param id    The ID of the object.
        @param file_name    The file name of the sprite image.
        @param name    The display name of the object.
        """
        super().__init__()


        self.default_surface = pygame.transform.smoothscale(pygame.image.load(os.path.join("..", "media", file_name)).convert(), (width, height))
        self.surface = self.default_surface
        self.image = self.surface

        self.setX(x)
        self.setY(y)
        self.width = width
        self.height = height
        self.setRotation(r)
        self.ID = id
        self.name = name

        # pygame.draw.rect(self.image, color, pygame.Rect(self.xPos(), self.yPos(), self.width, self.height))

        self.rect = self.surface.get_rect()

        self.update_sprite()

    def setX(self, x: int): self.X = x
    def setY(self, y: int): self.Y = y
    def setRotation(self, r: float):
        self.R = r
        self.surface = pygame.transform.rotate(self.default_surface, self.R)
        self.rect = self.surface.get_rect()
        self.image = self.surface

    def xPos(self): return self.X
    def yPos(self): return self.Y
    def getRotation(self): return self.R

    def update_sprite(self):
        self.rect.x = self.xPos() - (self.width // 2)
        self.rect.y = self.yPos() - (self.height // 2)

class Circle:
    def __init__(self, center: tuple, mass: float, id: int, time_increment: float):
        """
        @brief    Base class Circle used to store basic data for elements rendered to the screen as
                  shapes drawn by pygame pre-built functions.
        @param center    A tuple containing the x and y coordinates of the center of the circle.
        @param mass    The mass of the circle.
        @param id    The id of the Circle instance.
        @param time_increment    The increment of time in seconds to use when processing physics.
        """
        self.center = [center[0], center[1]]
        self.xPos = float(center[0])
        self.yPos = float(center[1])
        self.dt = time_increment
        self.inContact = False
        self.setDisplayCoords(center[0], center[1])
        self.setMass(mass)
        self.ID = id
        self.acceleration = [0.0, 9.8 * self.dt]
        self.velocity = [0.0, 0.0]
    
    def setMass(self, mass: float):
        """
        @brief    Sets the mass of the Circle, and changes other attributes like size and color
                  depending on that mass.
        @param mass    The value to set as the mass.
        """
        self.mass = mass
        if mass < 3.0:
            self.color = (255, 0, 0)
            self.radius = 15
        elif mass < 5.0:
            self.color = (0, 255, 0)
            self.radius = 30
        elif mass < 10.0:
            self.color = (0, 0, 255)
            self.radius = 45
        else:
            self.color = (0, 0, 0)
            self.radius = 100
    
    def process_physics(self):
        """
        @brief    Changes the Circle's position based on its given acceleration and velocity
                  vectors.
        """
        # self.inContact = False
        print(self.acceleration[1])
        if not self.inContact and self.xPos - self.radius < 0:
            self.inContact = True
            self.acceleration[0] = 10
        elif not self.inContact and self.xPos + self.radius > 800:
            self.inContact = True
            self.acceleration[0] = -10
        elif not self.inContact and self.yPos - self.radius < 0:
            self.inContact = True
            self.acceleration[1] = 10
        elif not self.inContact and self.yPos + self.radius > 800:
            self.inContact = True
            self.acceleration[1] = -10
        else:
            self.inContact = False



        # For x-position
        self.velocity[0] = float(self.acceleration[0] + self.velocity[0])
        self.xPos = float((self.acceleration[0] / 2) +\
                           self.velocity[0] + self.xPos)

        # For y-position
        self.velocity[1] = float(self.acceleration[1] + self.velocity[1])
        self.yPos = float((self.acceleration[1] / 2) +\
                           self.velocity[1] + self.yPos)
        
        
        
        self.setDisplayCoords(self.xPos, self.yPos)

    def setDisplayCoords(self, x: float, y: float):
        self.center[0] = round(x)
        self.center[1] = round(y)