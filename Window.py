import pygame as pygame
from objects.objects import Sprite

class Window:    
    def __init__(self, title: str, background_color, window_width: int, window_height: int):
        """
        @brief    GUI management class that handles rendering only.
        @param    The title of the window.
        @param background_color    A triplet containing RGB values for the background of the window
                                   (0-255).
        @param window_width    The width of the window to display.
        @param window_height    The height of the window to display.
        """
        self.dimensions = (window_width, window_height)
        self.background_color = background_color
        pygame.init()
        self.screen = pygame.display.set_mode(self.dimensions, pygame.RESIZABLE)
        pygame.display.set_caption(title)
        self.tick = pygame.time.Clock()
        self.isRunning = True

    def update(self, sprite_list: pygame.sprite.Group()):
        sprite_list.update()
        self.screen.fill(self.background_color)
        sprite_list.draw(self.screen)
        pygame.display.flip()

    def quit(self):
        pygame.quit()

    
