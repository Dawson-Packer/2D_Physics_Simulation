import pygame as pygame
import objects.objects as obj
import CollisionDetection as cd
import random as rd

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
        @brief    Runs all functions in the program necessary in one iteration.
        @param time_passed    The time passed since last execution.
        """
        # for shape in self.shape_list:
        #     if not shape.inContact:
        #         # print("reset")
        #         shape.acceleration[0] = 0.0
        #         shape.acceleration[1] = 9.8
        cd.handle_collisions(self.objects_list)


        for object in self.objects_list:
            if type(object) is obj.CollisionObject: object.process_physics()



        # for shape in self.shape_list:
        #     shape.process_physics(time_passed)

        self.sprite_list.update()
       
    def setup(self):
        """
        @brief    Function to setup specific programlogic class components for this program, 
                  like objects.
        """
        self.sprite_list = pygame.sprite.Group()
        self.objects_list = []


        self.background = obj.Sprite(800, 800, 400, 400, 0.0, -1, "background.png", "Background")
        self.sprite_list.add(self.background)
        # TODO: Randomize starting positions and velocities
        # self.objects_list.append(obj.CollisionObject((400, 400), 0, 1.5, 15.0, 2.0, "blue_ball.png", "Blue 1"))
        # self.objects_list.append(obj.CollisionObject((200, 100), 1, 3.2, -2.0, 0.5, "green_ball.png", "Green 1"))
        # self.objects_list.append(obj.CollisionObject((450, 600), 2, 5.5, -35.0, -5.0, "blue_ball.png", "Blue 2"))
        # self.objects_list.append(obj.CollisionObject((200, 700), 3, 4.0, 16.0, -12.0, "pink_ball.png", "Pink 1"))
        # self.objects_list.append(obj.CollisionObject((300, 100), 4, 3.2, -20.0, 0.12, "green_ball.png", "Green 2"))
        # self.objects_list.append(obj.CollisionObject((150, 600), 5, 5.5, -65.0, -51.0, "blue_ball.png", "Blue 3"))
        # self.objects_list.append(obj.CollisionObject((700, 700), 6, 4.0, 6.0, -42.0, "pink_ball.png", "Pink 2"))
        # self.objects_list.append(obj.CollisionObject((250, 600), 5, 5.5, -65.0, -51.0, "blue_ball.png", "Blue 4"))
        # self.objects_list.append(obj.CollisionObject((600, 700), 6, 4.0, 6.0, -42.0, "pink_ball.png", "Pink 3"))
        for j in range(0, 1):
            for i in range(0, 20):
                self.objects_list.append(obj.CollisionObject((rd.randint(50, 750), 
                                                            rd.randint(50, 750)), i, 
                                                            rd.randint(0, 4) + rd.random(), 
                                                            rd.randint(-50, 50) + rd.random(),
                                                            rd.randint(-50, 50) + rd.random(),
                                                            "blue_ball.png", "Blue " + str(i)))
            for i in range(20, 40):
                self.objects_list.append(obj.CollisionObject((rd.randint(50, 750),
                                                            rd.randint(50, 750)), i,
                                                            rd.randint(0, 4) + rd.random(),
                                                            rd.randint(-50, 50) + rd.random(),
                                                            rd.randint(-50, 50) + rd.random(),
                                                            "green_ball.png", "Green " + str(i)))
            for i in range(40, 60):
                self.objects_list.append(obj.CollisionObject((rd.randint(50, 750),
                                                            rd.randint(50, 750)), i,
                                                            rd.randint(0, 4) + rd.random(),
                                                            rd.randint(-50, 50) + rd.random(),
                                                            rd.randint(-50, 50) + rd.random(),
                                                            "pink_ball.png", "Pink " + str(i)))
            
        for object in self.objects_list:
            self.sprite_list.add(object)