from window import *
from programlogic import *

class application:
    def __init__(self, title: str, dim_width: int, dim_height: int):
        self.title = title
        self.dimensions = (dim_width, dim_height)
        self.wd = window(title, (200, 200, 200), self.dimensions[0], self.dimensions[1])
        self.pl = programlogic(dim_width, dim_height, (0, 0))
        self.isRunning = self.wd.isRunning
        self.delay = self.pl.time_increment # Mainloop delay in seconds
    
    def tick(self):
        
        self.process_inputs()
        self.pl.tick()
        
        self.wd.update(self.pl.objects_list, self.pl.shape_list)

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