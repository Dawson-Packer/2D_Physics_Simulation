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
        # for shape in self.shape_list:
        #     if not shape.inContact:
        #         # print("reset")
        #         shape.acceleration[0] = 0.0
        #         shape.acceleration[1] = 9.8

        for object in self.objects_list:
            if type(object) is obj.CollisionObject: object.process_physics()


        # for shape in self.shape_list:
        #     shape.process_physics(time_passed)

        self.objects_list.update()
       
    def setup(self):
        """
        @brief    Function to setup specific programlogic class components for this program, 
                  like objects.
        """
        self.objects_list = pygame.sprite.Group()
        self.shape_list = []


        self.background = obj.Sprite(800, 800, 400, 400, 0.0, -1, "background.png", "Background")
        self.objects_list.add(self.background)
        self.objects_list.add(obj.CollisionObject((400, 400), 0, 1.5, 15.0, 2.0, "blue_ball.png", ""))
        self.objects_list.add(obj.CollisionObject((200, 100), 1, 3.2, -2.0, 0.5, "green_ball.png", ""))
        self.objects_list.add(obj.CollisionObject((450, 600), 2, 5.5, -35.0, -5.0, "blue_ball.png", ""))
        self.objects_list.add(obj.CollisionObject((200, 700), 3, 4.0, 16.0, -12.0, "pink_ball.png", ""))