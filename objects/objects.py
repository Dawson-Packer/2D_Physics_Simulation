import pygame as pygame
import math as math
import os
import random

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def wall_collision(x_pos: int, y_pos: int, buffer: int, 
                   x_velocity: float, y_velocity: float) -> tuple:
    """
    @brief    Checks if the specified coordinates collide with a hardcoded box and responds.
    @param x_pos    The x-posiiton of the particle.
    @param y_pos    The y-position of the particle.
    @param buffer    The buffer width to calculate collisions at.
    @param x_velocity    The x-velocity to modify.
    @param y_velocity    The y-velocity to modify.
    @return Returns a tuple containing the updated x- and y-velocity.
    """
    velocity = [x_velocity, y_velocity]
    if x_pos - buffer < 0 or x_pos + buffer > 800: velocity[0] = -velocity[0]
    if y_pos - buffer < 0 or y_pos + buffer > 800: velocity[1] = -velocity[1]
    return velocity




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

        self.set_x(x)
        self.set_y(y)
        self.width = width
        self.height = height
        self.set_rotation(r)
        self.ID = id
        self.name = name

        # pygame.draw.rect(self.image, color, pygame.Rect(self.xPos(), self.yPos(), self.width, self.height))

        self.rect = self.surface.get_rect()

        self.update_sprite()

    def set_x(self, x: int): self.X = x
    def set_y(self, y: int): self.Y = y
    def set_rotation(self, r: float):
        self.R = r
        self.surface = pygame.transform.rotate(self.default_surface, self.R)
        self.rect = self.surface.get_rect()
        self.image = self.surface

    def x_pos(self): return self.X
    def y_pos(self): return self.Y
    def get_rotation(self): return self.R

    def update_sprite(self):
        self.rect.x = self.x_pos() - (self.width // 2)
        self.rect.y = self.y_pos() - (self.height // 2)

class Shape:
    def __init__(self, center: tuple, id: int):
        """
        @brief    Base class Shape for drawing pygame shapes to the screen.
        @param center    A tuple containing the x and y coordinates of the center of the circle.
        @param id    The ID of the Shape instance.
        """
        self.center = [0, 0]
        self.x_pos = float(center[0])
        self.y_pos = float(center[1])
        self.ID = id
        self.color = (0, 0, 0)
        self.radius = None
        self.set_display_coords(center[0], center[1])
        
    def set_display_coords(self, x: float, y: float):
        self.center[0] = round(x)
        self.center[1] = round(y)
        
class CollisionObject(Shape):
    def __init__(self, center: tuple, id: int, mass: float, x_velocity: float, y_velocity: float):
        """
        @brief    CollisionObject class containing data and methods necessary to track colliding
                  circles on the screen.
        @param center    A tuple containing the x and y coordinates of the center of the circle.
        @param id    The ID of the Shape instance.
        @param mass    The mass of the circle.
        @param x_velocity    The initial x_velocity of the CollisionObject.
        @param y_velocity    The initial y_velocity of the CollisionObject.
        """
        super().__init__(center, id)
        self.set_mass(mass)
        self.previous_x_pos = None
        self.previous_y_pos = None
        self.velocity = [x_velocity, y_velocity]
        self.inContact = False
    
    def set_mass(self, mass: float):
        """
        @brief    Sets the mass of the Circle, and changes other attributes like size and color
                  depending on that mass.
        @param mass    The value to set as the mass.
        """
        self.mass = mass
        if mass < 3.0:
            self.color = (0, 214, 56)
            self.radius = 20
        elif mass < 5.0:
            self.color = (0, 191, 186)
            self.radius = 20
        elif mass < 10.0:
            self.color = (0, 7, 249)
            self.radius = 20
        else:
            self.color = (227, 0, 131)
            self.radius = 20

    def process_physics(self):
        self.velocity[0], self.velocity[1] = wall_collision(self.x_pos, self.y_pos, self.radius + 1, 
                                                            self.velocity[0], self.velocity[1])
        self.x_pos += self.velocity[0]
        self.y_pos += self.velocity[1]
        self.previous_x_pos = self.x_pos
        self.previous_y_pos = self.y_pos
        self.set_display_coords(self.x_pos, self.y_pos)


class PhysicsObject(Shape):
    def __init__(self, center: tuple, mass: float, id: int):
        """
        @brief    Base class Circle used to store basic data for elements rendered to the screen as
                  shapes drawn by pygame pre-built functions.
        @param center    A tuple containing the x and y coordinates of the center of the circle.
        @param mass    The mass of the circle.
        @param id    The id of the Circle instance.
        """
        super().__init__(center, id)
        self.inContact = False
        self.set_mass(mass)
        self.acceleration = [0.0, 9.8]
        self.velocity = [0.0, 0.0]
    
    def set_mass(self, mass: float):
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
    
    def process_physics(self, dt: int):
        """
        @brief    Changes the Circle's position based on its given acceleration and velocity
                  vectors.
        @param dt    The change in time since last update (in seconds).
        """
        if self.x_pos - self.radius < 0 or self.x_pos + self.radius > 800:
            if (not self.inContact) and abs(self.velocity[0]) > 1e-4: self.velocity[0] = -self.velocity[0]
            self.inContact = True
        elif self.y_pos - self.radius < 0 or self.y_pos + self.radius > 800:
            if (not self.inContact) and abs(self.velocity[1]) > 1e-4: self.velocity[1] = -self.velocity[1]
            self.inContact = True
        else:
            self.inContact = False
        
        if abs(self.velocity[0]) < 1e-4 or abs(self.velocity[1]) < 1e-4:
            if abs(self.velocity[0]) < 1e-4: 
                self.velocity[0] = 0.0
            if abs(self.velocity[1]) < 1e-4: self.velocity[1] = 0.0

        
        # print(self.velocity[1])
        # For x-position
        self.velocity[0] = float(self.acceleration[0]*dt + self.velocity[0])
        self.x_pos = float((self.acceleration[0] / 2)*(dt**2) +\
                           self.velocity[0]*dt + self.x_pos)

        # For y-position
        self.velocity[1] = float(self.acceleration[1]*dt + self.velocity[1])
        self.y_pos = float((self.acceleration[1] / 2)*(dt**2) +\
                           self.velocity[1]*dt + self.y_pos)
        
        
        
        self.set_display_coords(self.x_pos, self.y_pos)

class VectorArrow(Shape):
    pass