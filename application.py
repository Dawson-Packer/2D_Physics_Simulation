from Window import *
from ProgramLogic import *

class Application:
    def __init__(self, title: str, dim_width: int, dim_height: int):
        self.title = title
        self.dimensions = (dim_width, dim_height)
        self.wd = Window(title, (200, 200, 200), self.dimensions[0], self.dimensions[1])
        self.pl = ProgramLogic(dim_width, dim_height, (0, 0))
        self.isRunning = self.wd.isRunning
        self.delay = 0.001 # seconds
        self.game_tick = 0
        self.window_tick = 0
    
    def tick(self):
        
        self.game_tick += 1
        self.window_tick += 1
        if self.game_tick == 1:
            self.process_inputs()
            self.pl.tick(0.02)
            self.game_tick = 0
        
        if self.window_tick == 17:
            self.wd.update(self.pl.objects_list, self.pl.shape_list)
            self.window_tick = 0

    def process_inputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            pass
        elif keys[pygame.K_RIGHT]:
            pass

    def quit(self):
        self.wd.quit()
        self.isRunning = False