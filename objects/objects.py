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




class Sprite(pygame.sprite.Sprite):
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


        self.default_surface = pygame.transform.smoothscale(pygame.image.load(os.path.join("..", "media", file_name)).convert_alpha(), (width, height))
        self.surface = self.default_surface
        self.image = self.surface

        self.set_display_x(x)
        self.set_display_y(y)
        self.width = width
        self.height = height
        self.set_rotation(r)
        self.ID = id
        self.name = name

        # pygame.draw.rect(self.image, color, pygame.Rect(self.xPos(), self.yPos(), self.width, self.height))

        self.rect = self.surface.get_rect()

        self.update_sprite(self.X, self.Y)

    def set_display_x(self, x: float): self.X = round(x)
    def set_display_y(self, y: float): self.Y = round(y)
    def set_rotation(self, r: float):
        self.R = r
        self.surface = pygame.transform.rotate(self.default_surface, self.R)
        self.rect = self.surface.get_rect()
        self.image = self.surface

    def display_x(self): return self.X
    def display_y(self): return self.Y
    def get_rotation(self): return self.R

    def update_sprite(self, x: float, y: float):
        self.set_display_x(x)
        self.set_display_y(y)
        self.rect.x = self.display_x() - (self.width // 2)
        self.rect.y = self.display_y() - (self.height // 2)
        
class CollisionObject(Sprite):
    def __init__(self, center: tuple, id: int, mass: float, x_velocity: float, y_velocity: float,
                 file_name: str, name: str):
        """
        @brief    CollisionObject class containing data and methods necessary to track colliding
                  circles on the screen.
        @param center    A tuple containing the x and y coordinates of the center of the circle.
        @param id    The ID of the Shape instance.
        @param mass    The mass of the circle.
        @param x_velocity    The initial x_velocity of the CollisionObject.
        @param y_velocity    The initial y_velocity of the CollisionObject.
        @param file_name    The name of the file to use as its texture.
        @param name    The reference name of the Sprite.
        """
        self.set_mass(mass)
        super().__init__(self.radius * 2, self.radius * 2, 
                         center[0], center[1], 0.0, id, file_name, name)
        self.x_pos, self.y_pos = center
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
        if mass < 3.0: self.radius = 20
        elif mass < 5.0: self.radius = 20
        elif mass < 10.0: self.radius = 20
        else: self.radius = 20

    def process_physics(self):
        self.velocity[0], self.velocity[1] = wall_collision(self.x_pos, self.y_pos, self.radius + 1, 
                                                            self.velocity[0], self.velocity[1])
        self.x_pos += self.velocity[0]
        self.y_pos += self.velocity[1]
        self.previous_x_pos = self.x_pos
        self.previous_y_pos = self.y_pos
        self.update_sprite(self.x_pos, self.y_pos)

    def convert_position_to_display(self):
        self.set_display_x(self.x_pos)
        self.set_display_y(self.y_pos)