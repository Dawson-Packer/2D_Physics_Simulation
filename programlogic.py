import pygame as pygame
import objects.objects as obj

class ProgramLogic:
    def __init__(self, field_width: int, field_height: int, offset: tuple):
        """
        @brief    The program handling, controls program objects and event functions.
        @param field_width    The width of the available space to plot.
        @param field_height    The height of the available space to plot.
        @param offset    The x and y offset from the corner of the screen to set the local
                         coordinate axii.
        """
        self.isRunning = True
        # self.time_increment = 0.020
        self.shape_vectors = {}
        self.field_width = field_width
        self.field_height = field_height
        self.setup()

    def tick(self, time_passed: int):
        """
        @brief    Runs all functions in the program necessary in one iteration
        @param time_passed    The time passed since last execution
        """
        for shape in self.shape_list:
            if not shape.inContact:
                # print("reset")
                shape.acceleration[0] = 0.0
                # shape.acceleration[1] = 9.8



        for shape in self.shape_list:
            shape.process_physics(time_passed)

        self.objects_list.update()
       
    def setup(self):
        """
        @brief    Function to setup specific programlogic class components for this program, 
                  like objects.
        """
        self.objects_list = pygame.sprite.Group()
        self.shape_list = []


        self.background = obj.Object(800, 800, 400, 400, 0.0, -1, "background.png", "Background")
        self.objects_list.add(self.background)
        self.shape_list.append(obj.Circle((400, 400), 4.5, 0))



    